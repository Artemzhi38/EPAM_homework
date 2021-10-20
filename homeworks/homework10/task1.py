"""Ваша задача спарсить информацию о компаниях, находящихся в индексе S&P 500 с
 данного сайта:
https://markets.businessinsider.com/index/components/s&p_500

Для каждой компании собрать следующую информацию:

Текущая стоимость в рублях (конвертацию производить по текущему курсу, взятому
с сайта центробанка РФ)
Код компании (справа от названия компании на странице компании)
P/E компании (информация находится справа от графика на странице компании)
Годовой рост/падение компании в процентах (основная таблица)
Высчитать какую прибыль принесли бы акции компании (в процентах), если бы они
были куплены на уровне 52 Week Low и проданы на уровне 52 Week High (справа от
графика на странице компании)
Сохранить итоговую информацию в 4 JSON файла:

Топ 10 компаний с самими дорогими акциями в рублях.
Топ 10 компаний с самым низким показателем P/E.
Топ 10 компаний, которые показали самый высокий рост за последний год
Топ 10 комппаний, которые принесли бы наибольшую прибыль, если бы были куплены
на самом минимуме и проданы на самом максимуме за последний год.
Пример формата:
[
    {
        "code": "MMM",
        "name": "3M CO.",
        "price" | "P/E" | "growth" | "potential profit" : value,
    },
    ...
]
For scrapping you cans use beautifulsoup4
For requesting aiohttp"""
import asyncio
import json
import os
import aiohttp
import requests
from bs4 import BeautifulSoup


def usd_cb_course():
    """function to get current cb usd to rub course"""
    resp = requests.get('http://www.cbr.ru/scripts/XML_daily.asp')
    bs = BeautifulSoup(resp.text, 'html.parser')
    return round(float(bs.find("name", string="Доллар США").
                       next_element.next_element.string.replace(',', '.')), 2)


def company_code(bs):
    """filter func to find company code on company page"""
    return (bs.find("span", class_="price-section__category").
            next_element.next_element.string[2:])


def company_name(bs):
    """filter func to find company name on company page"""
    return bs.find("span", class_="price-section__label").string.strip()


def pe_ratio(bs):
    """filter func to find company P/E ratio on company page
       returns 0 if there is no P/E ratio for this company"""
    try:
        return float(bs.find(
            "div", class_="snapshot__header", string="P/E Ratio"
        ).previous_element.strip().replace(',', ''))
    except AttributeError:
        return 0


def percent_profit(bs):
    """filter func to find company potential profit based on 52
       Week Low and 52 Week High parametres on company page
       returns 0 if there are o such parametres for this company"""
    try:
        week_low = bs.find(
            "div", class_="snapshot__header",
            string="52 Week Low"
        ).previous_element.strip().replace(',', '')
        week_high = bs.find(
            "div", class_="snapshot__header",
            string="52 Week High"
        ).previous_element.strip().replace(',', '')
        return round((float(week_high)-float(week_low))*100/float(week_low), 2)
    except AttributeError:
        return 0


def price_in_rubles(bs, cb_course):
    """func to find company price on company page and convert
       it to rubles by current cb usd-to-rub course"""
    usd_price = float(bs.find(
        "span", class_="price-section__current-value"
    ).string.replace(',', ''))
    return round(cb_course*usd_price, 2)


async def all_companies(index_page_url):
    """async coroutine that finds all company-pages on
       one page of S&P 500 index list"""

    def companies_on_page(tag):
        """filter func to find all companies on index list page"""
        return (tag.name == "a"
                and tag.has_attr('href')
                and tag.has_attr('title')
                and not tag.has_attr('class'))

    async with aiohttp.ClientSession() as session:
        async with session.get(index_page_url) as index_page:
            index_page_text = await index_page.text()
            index_page_soup = BeautifulSoup(index_page_text, 'html.parser')
            return index_page_soup.findAll(companies_on_page)


async def fill_company(company, cb_course):
    """async coroutine that fills dict with all needed company parametres"""
    # fetch company page
    base_url = 'https://markets.businessinsider.com'
    company_page_url = base_url + company.attrs["href"]
    # found company year growth
    year_growth = float(company.parent.parent.
                        contents[-2].contents[-2].string[:-1])
    async with aiohttp.ClientSession() as session:
        async with session.get(company_page_url) as company_page:
            company_page_text = await company_page.text()
            company_soup = BeautifulSoup(company_page_text, 'html.parser')
            # found company code
            code = company_code(company_soup)
            # found company name
            name = company_name(company_soup)
            # found p/e ratio
            pe = pe_ratio(company_soup)
            # found potential profit
            profit = percent_profit(company_soup)
            #  found price in rubles
            price_rub = price_in_rubles(company_soup, cb_course)
            # filling company dict
            company_dict = {"code": code, "name": name, "price": price_rub,
                            "P/E": pe, "growth": year_growth,
                            "potential profit": profit}
            return company_dict


async def main_for_href(pages_urls, companies_list):
    """async event-loop that finds all hrefs for company pages"""
    tasks = [asyncio.create_task(all_companies(index_page_url))
             for index_page_url in pages_urls]
    loop = asyncio.gather(*tasks)
    await loop
    for task in tasks:
        companies_list.extend(task.result())


async def main_to_parse(companies_list, companies_dicts, cb_course):
    """async event-loop to parse all companies pages"""
    tasks = [asyncio.create_task(fill_company(company, cb_course))
             for company in companies_list]
    loop = asyncio.gather(*tasks)
    await loop
    for task in tasks:
        companies_dicts.append(task.result())


def top_highest_price(dicts):
    """func that finds top-10 companies with highest price"""
    dicts.sort(key=lambda x: x['price'], reverse=True)
    return dicts[:10]


def top_lowest_pe(dicts):
    """func that finds top-10 companies with lowest pe"""
    return sorted(sorted(dicts, key=lambda x: x['P/E']),
                  key=lambda x: x['P/E'] == 0)[:10]


def top_highest_growth(dicts):
    """func that finds top-10 companies with highest growth"""
    dicts.sort(key=lambda x: x['growth'], reverse=True)
    return dicts[:10]


def top_highest_potential_profit(dicts):
    """func that finds top-10 companies with highest potential profit"""
    dicts.sort(key=lambda x: x['potential profit'], reverse=True)
    return dicts[:10]


def tops_to_json(companies_data):
    """func to create 4 json files with top-10 of companies"""
    file_names = ['highest_price.json', 'lowest_pe.json',
                  'highest_growth.json', 'highest_potential_profit.json']
    funcs = [top_highest_price, top_lowest_pe, top_highest_growth,
             top_highest_potential_profit]
    name_func = dict(zip(file_names, funcs))
    for name, func in name_func.items():
        with open(name, 'w') as result_file:
            result_file.write(json.dumps(func(companies_data), indent=4))


def main():
    # preparation part
    current_cb_course = usd_cb_course()
    index_url = 'https://markets.businessinsider.com/index/components/s&p_500'
    all_index_pages_urls = [index_url + f'?p={i}' for i in range(1, 12)]
    companies = []
    companies_dicts_list = []
    if os.name == 'nt':
        asyncio.set_event_loop_policy(asyncio.
                                      WindowsSelectorEventLoopPolicy())
    # async part
    asyncio.run(main_for_href(all_index_pages_urls, companies))
    asyncio.run(main_to_parse(companies[:175], companies_dicts_list,
                              current_cb_course))
    asyncio.run(main_to_parse(companies[175:350], companies_dicts_list,
                              current_cb_course))
    asyncio.run(main_to_parse(companies[350:], companies_dicts_list,
                              current_cb_course))
    # result part
    tops_to_json(companies_dicts_list)


if __name__ == '__main__':
    main()
