import sqlite3

from homeworks.homework8.task2 import TableData


def test_len_method():
    """Testing that len(table_name) will give current amount of rows in table
    in database"""
    presidents = TableData('example.sqlite', 'presidents')
    books = TableData('example.sqlite', 'books')
    assert len(presidents) == 3
    assert len(books) == 3


def test_getitem_method():
    """Testing that any row of oject is acessible as collection item with
    value of row's 'name' column"""
    books = TableData('example.sqlite', 'books')
    assert books['1984'] == {'name': '1984', 'author': 'Orwell'}


def test_contains_method():
    """Testing that code 'name_value in TableData(database_name, table_name)'
     returns if row with same name exists in table"""
    presidents = TableData('example.sqlite', 'presidents')
    assert 'Yeltsin' in presidents
    assert 'Stalin' not in presidents


def test_iter_method():
    """Testing that TableData-class object implements iteration protocol.
    i.e. you could use it in for loops"""
    presidents = TableData('example.sqlite', 'presidents')
    list_of_names = []
    for president in presidents:
        list_of_names.append(president['name'])
    assert len(list_of_names) == len(presidents)


def test_receiving_most_recent_data_from_database():
    """Testing that all methods of TableData-class object reflect most
    recent data. If data in table was changed after creation of collection
     instance, all calls should return updated data"""
    presidents = TableData('example.sqlite', 'presidents')
    with sqlite3.connect('example.sqlite') as conn:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO presidents VALUES ('Stalin', 1953,'USSR')")
    assert len(presidents) == 4
    assert 'Stalin' in presidents
    assert presidents['Stalin'] == {'name': 'Stalin', 'age': 1953,
                                    'country': 'USSR'}
    list_of_names = []
    for president in presidents:
        list_of_names.append(president['name'])
    assert len(list_of_names) == len(presidents)
    with sqlite3.connect('example.sqlite') as conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM presidents WHERE name = 'Stalin'")
