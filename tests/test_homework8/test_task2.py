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


def test_contains_method():
    """Testing that code 'name_value in TableData(database_name, table_name)'
     returns if row with same name exists in table"""


def test_iter_method():
    """Testing that TableData-class object implements iteration protocol.
    i.e. you could use it in for loops"""


def test_recieving_most_recent_data_from_database():
    """Testing that all methods of TableData-class object reflect most
    recent data. If data in table was changed after creation of collection
     instance, all calls should return updated data"""


cursor.execute('SELECT * from books')
data = cursor.fetchall()   # will be a list with data.
print(data)

cursor.execute('SELECT * from presidents')
data = cursor.fetchall()   # will be a list with data.
print(data)
print()

presidents_td = TableData('example.sqlite', 'presidents')
books_td = TableData('example.sqlite', 'books')
print(len(presidents_td), len(books_td))
print('Yeletsin' in presidents_td)
print(books_td['1984'])
for book in books_td:
    print(book)