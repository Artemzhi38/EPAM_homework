import ast
import os

import pytest
import requests

from bs4 import BeautifulSoup

from homeworks.homework10.task1 import (all_companies, company_code,
                                        company_name, fill_company, pe_ratio,
                                        percent_profit, price_in_rubles,
                                        top_highest_growth,
                                        top_highest_potential_profit,
                                        top_highest_price, top_lowest_pe,
                                        tops_to_json, usd_cb_course)


@pytest.fixture()
def dict_list_fixture():
    di = [
        {'code': 'MMM', 'name': '3M Co.', 'price': 12935.7,
         'P/E': 19.91, 'growth': 6.71, 'potential profit': 33.81},
        {'code': 'AOS', 'name': 'A.O. Smith Corp.', 'price': 4647.12,
         'P/E': 25.06, 'growth': 17.0, 'potential profit': 44.59},
        {'code': 'ABT', 'name': 'Abbott Laboratories', 'price': 8480.21,
         'P/E': 29.76, 'growth': 9.62, 'potential profit': 25.71},
        {'code': 'ABBV', 'name': 'AbbVie Inc', 'price': 7632.11,
         'P/E': 9.91, 'growth': 27.88, 'potential profit': 53.58},
        {'code': 'ABMD', 'name': 'ABIOMED Inc.', 'price': 24797.63,
         'P/E': 63.24, 'growth': 21.69, 'potential profit': 59.6},
        {'code': 'ACN', 'name': 'Accenture plc', 'price': 24819.63,
         'P/E': 32.42, 'growth': 48.19, 'potential profit': 65.03},
        {'code': 'ATVI', 'name': 'Activision Blizzard Inc.', 'price': 5477.46,
         'P/E': 26.4, 'growth': -5.28, 'potential profit': 46.83},
        {'code': 'ADBE', 'name': 'Adobe Inc.', 'price': 45141.89,
         'P/E': 47.1, 'growth': 21.22, 'potential profit': 60.15},
        {'code': 'AAP', 'name': 'Advance Auto Parts Inc.', 'price': 15924.96,
         'P/E': 18.27, 'growth': 36.57, 'potential profit': 58.2},
        {'code': 'AES', 'name': 'AES Corp.', 'price': 1711.8,
         'P/E': 15.98, 'growth': 22.24, 'potential profit': 53.16},
        {'code': 'AFL', 'name': 'Aflac Inc', 'price': 3961.55,
         'P/E': 8.88, 'growth': 48.74, 'potential profit': 72.73},
        {'code': 'A', 'name': 'Agilent Technologies Inc.', 'price': 11049.32,
         'P/E': 30.64, 'growth': 44.94, 'potential profit': 78.41},
        {'code': 'APD', 'name': 'Air Products and Chemicals Inc.',
         'price': 20902.08, 'P/E': 35.81, 'growth': -2.63,
         'potential profit': 33.42},
        {'code': 'AKAM', 'name': 'Akamai Inc.', 'price': 7659.08,
         'P/E': 20.32, 'growth': -3.47, 'potential profit': 34.83},
        {'code': 'ALK', 'name': 'Alaska Air Group Inc.', 'price': 4036.77,
         'P/E': -5.1, 'growth': 51.35, 'potential profit': 111.78},
        {'code': 'ALB', 'name': 'Albemarle Corp.', 'price': 16724.79,
         'P/E': 35.35, 'growth': 145.44, 'potential profit': 181.0},
        {'code': 'ARE', 'name': 'Alexandria Real Estate Equities Inc.',
         'price': 14425.36, 'P/E': 28.92, 'growth': 24.11,
         'potential profit': 39.71},
        {'code': 'ALGN', 'name': 'Align Technology Inc.', 'price': 42175.34,
         'P/E': 98.94, 'growth': 77.54, 'potential profit': 128.4},
        {'code': 'ALLE', 'name': 'Allegion PLC', 'price': 9559.66,
         'P/E': 0, 'growth': 26.33, 'potential profit': 55.3},
        {'code': 'LNT', 'name': 'Alliant Energy Corp.', 'price': 3950.9,
         'P/E': 20.65, 'growth': 2.91, 'potential profit': 35.57}
    ]
    return di


def test_percent_profit():
    mmm_url = 'https://markets.businessinsider.com/stocks/mmm-stock'
    mmm_page_text = requests.get(mmm_url).text
    mmm_soup = BeautifulSoup(mmm_page_text, 'html.parser')
    try:
        week_low = mmm_soup.find(
            "div", class_="snapshot__header",
            string="52 Week Low"
        ).previous_element.strip().replace(',', '')
        week_high = mmm_soup.find(
            "div", class_="snapshot__header",
            string="52 Week High"
        ).previous_element.strip().replace(',', '')
        res = round((float(week_high)-float(week_low))*100/float(week_low), 2)
    except AttributeError:
        res = 0
    assert percent_profit(mmm_soup) == res


def test_usd_cb_course():
    """Testing that function returns positive float"""
    result = usd_cb_course()
    assert isinstance(result, float)
    assert result > 0


def test_company_code():
    mmm_url = 'https://markets.businessinsider.com/stocks/mmm-stock'
    mmm_page_text = requests.get(mmm_url).text
    mmm_soup = BeautifulSoup(mmm_page_text, 'html.parser')
    assert company_code(mmm_soup) == 'MMM'


def test_company_name():
    mmm_url = 'https://markets.businessinsider.com/stocks/mmm-stock'
    mmm_page_text = requests.get(mmm_url).text
    mmm_soup = BeautifulSoup(mmm_page_text, 'html.parser')
    assert company_name(mmm_soup) == '3M Co.'


def test_pe_ratio():
    mmm_url = 'https://markets.businessinsider.com/stocks/mmm-stock'
    mmm_page_text = requests.get(mmm_url).text
    mmm_soup = BeautifulSoup(mmm_page_text, 'html.parser')
    try:
        res = float(mmm_soup.find(
            "div", class_="snapshot__header", string="P/E Ratio"
        ).previous_element.strip().replace(',', ''))
    except AttributeError:
        res = 0
    assert pe_ratio(mmm_soup) == res


def test_price_in_rubles():
    mmm_url = 'https://markets.businessinsider.com/stocks/mmm-stock'
    mmm_page_text = requests.get(mmm_url).text
    mmm_soup = BeautifulSoup(mmm_page_text, 'html.parser')
    res = round(1*float(mmm_soup.find("span",
                                      class_="price-section__current-value"
                                      ).string.replace(',', '')), 2)
    assert price_in_rubles(mmm_soup, 1) == res


def test_top_highest_price(dict_list_fixture):
    """Testing that function returns right list of
    top-10 when given a list of dicts"""
    assert top_highest_price(dict_list_fixture)[0] == {
        "code": "ADBE",
        "name": "Adobe Inc.",
        "price": 45141.89,
        "P/E": 47.1,
        "growth": 21.22,
        "potential profit": 60.15
    }
    assert top_highest_price(dict_list_fixture)[-1] == {
        "code": "A",
        "name": "Agilent Technologies Inc.",
        "price": 11049.32,
        "P/E": 30.64,
        "growth": 44.94,
        "potential profit": 78.41
    }


def test_top_lowest_pe(dict_list_fixture):
    """Testing that function returns right list of
    top-10 when given a list of dicts"""
    assert top_lowest_pe(dict_list_fixture)[0] == {
        "code": "ALK",
        "name": "Alaska Air Group Inc.",
        "price": 4036.77,
        "P/E": -5.1,
        "growth": 51.35,
        "potential profit": 111.78
    }
    assert top_lowest_pe(dict_list_fixture)[-1] == {
        "code": "ATVI",
        "name": "Activision Blizzard Inc.",
        "price": 5477.46,
        "P/E": 26.4,
        "growth": -5.28,
        "potential profit": 46.83
    }


def test_top_highest_growth(dict_list_fixture):
    """Testing that function returns right list of
    top-10 when given a list of dicts"""
    assert top_highest_growth(dict_list_fixture)[0] == {
        "code": "ALB",
        "name": "Albemarle Corp.",
        "price": 16724.79,
        "P/E": 35.35,
        "growth": 145.44,
        "potential profit": 181.0
    }
    assert top_highest_growth(dict_list_fixture)[-1] == {
        "code": "ARE",
        "name": "Alexandria Real Estate Equities Inc.",
        "price": 14425.36,
        "P/E": 28.92,
        "growth": 24.11,
        "potential profit": 39.71
    }


def test_top_highest_potential_profit(dict_list_fixture):
    """Testing that function returns right list of
    top-10 when given a list of dicts"""
    assert top_highest_potential_profit(dict_list_fixture)[0] == {
        "code": "ALB",
        "name": "Albemarle Corp.",
        "price": 16724.79,
        "P/E": 35.35,
        "growth": 145.44,
        "potential profit": 181.0
    }
    assert top_highest_potential_profit(dict_list_fixture)[-1] == {
        "code": "ALLE",
        "name": "Allegion PLC",
        "price": 9559.66,
        "P/E": 0,
        "growth": 26.33,
        "potential profit": 55.3
    }


def test_tops_to_json(dict_list_fixture):
    tops_to_json(dict_list_fixture)
    dictionary_example = {'code': 0, 'name': 0, 'price': 0, 'P/E': 0,
                          'growth': 0, 'potential profit': 0}
    file_names = ['highest_price.json', 'lowest_pe.json',
                  'highest_growth.json', 'highest_potential_profit.json']
    for file in file_names:
        with open(file) as f:
            string = f.read()
            result = ast.literal_eval(string)
            assert isinstance(result, list)
            assert isinstance(result[0], dict)
            assert result[0].keys() == dictionary_example.keys()
        os.remove(file)


@pytest.mark.asyncio
async def test_all_companies():
    url = 'https://markets.businessinsider.com/index/components/s&p_500?p=1'

    def companies_on_page(tag):
        return (tag.name == "a"
                and tag.has_attr('href')
                and tag.has_attr('title')
                and not tag.has_attr('class'))
    page_text = requests.get(url).text
    page_soup = BeautifulSoup(page_text, 'html.parser')
    reference = page_soup.findAll(companies_on_page)
    result = await all_companies(url)
    assert result == reference


@pytest.mark.asyncio
async def test_fill_company():
    dictionary_example = {'code': 0, 'name': 0, 'price': 0, 'P/E': 0,
                          'growth': 0, 'potential profit': 0}
    url = 'https://markets.businessinsider.com/index/components/s&p_500?p=1'
    companies = await all_companies(url)
    result = await fill_company(companies[0], usd_cb_course())
    assert isinstance(result, dict)
    assert result.keys() == dictionary_example.keys()
