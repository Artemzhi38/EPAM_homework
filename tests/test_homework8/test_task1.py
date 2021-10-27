import os.path

import pytest

from homeworks.homework8.task1 import KeyValueStorage


@pytest.fixture()
def int_values_fixture():
    path = os.path.join(os.path.dirname(__file__), 'task1.txt')
    with open(path, 'w') as test_file:
        test_file.writelines(["val1=1\n", "val2=0\n",
                              "val3=90.01\n", "val4=test\n"])
        return path


@pytest.fixture()
def access_fixture():
    path = os.path.join(os.path.dirname(__file__), 'task1.txt')
    with open(path, 'w') as test_file:
        test_file.writelines(["name=Ivan\n", "last_name=Ivanov\n",
                              "age=30\n", "country=Wonderland\n"])
        return path


@pytest.fixture()
def builtin_attributes_fixture():
    path = os.path.join(os.path.dirname(__file__), 'task1.txt')
    with open(path, 'w') as test_file:
        test_file.writelines(["__class__=attr1\n", "__dict__=attr2\n",
                              "__doc__=attr3\n", "__module__=attr4\n"])
        return path


@pytest.fixture()
def bad_string_fixture():
    path = os.path.join(os.path.dirname(__file__), 'task1.txt')
    with open(path, 'w') as test_file:
        test_file.writelines(["1=bad"])
        return path


@pytest.fixture()
def worse_string_fixture():
    path = os.path.join(os.path.dirname(__file__), 'task1.txt')
    with open(path, 'w') as test_file:
        test_file.writelines(["кириллица=worse"])
        return path


@pytest.fixture()
def worst_string_fixture():
    path = os.path.join(os.path.dirname(__file__), 'task1.txt')
    with open(path, 'w') as test_file:
        test_file.writelines(["test_%@^=worst"])
        return path


@pytest.fixture()
def builtin_key_fixture():
    path = os.path.join(os.path.dirname(__file__), 'task1.txt')
    with open(path, 'w') as test_file:
        test_file.writelines(["def=100"])
        return path


def test_int_values(int_values_fixture):
    """Testing that if a value can be treated both as a number
     and a string, it is treated as number"""
    storage = KeyValueStorage(int_values_fixture)
    print(int_values_fixture)
    print(storage)
    assert isinstance(storage['val1'], int)
    assert isinstance(storage['val2'], int)
    assert isinstance(storage['val3'], str)
    assert isinstance(storage['val4'], str)


def test_access_to_keys_and_values(access_fixture):
    """Testing that KeyValueStorage-class item has its keys
    and values accessible as collection items and as attributes"""
    storage = KeyValueStorage(access_fixture)
    assert storage['name'] == "Ivan"
    assert storage['last_name'] == "Ivanov"
    assert storage.age == 30
    assert storage.country == "Wonderland"


def test_builtin_attributes_have_priority(builtin_attributes_fixture):
    """Testing that in case of attribute clash existing
    built-in attributes take precedence"""
    storage = KeyValueStorage(builtin_attributes_fixture)
    assert not storage.__class__ == "attr1"
    assert not storage.__dict__ == "attr2"
    assert not storage.__doc__ == "attr3"
    assert not storage.__module__ == "attr4"


def test_value_starts_with_digit_cannot_be_assigned(bad_string_fixture):
    """Testing that in case when value cannot be assigned to
     an attribute ValueError should is raised."""
    with pytest.raises(ValueError):
        KeyValueStorage(bad_string_fixture)


def test_cirillic_value_cannot_be_assigned(worse_string_fixture):
    """Testing that in case when value cannot be assigned to
     an attribute ValueError should is raised."""
    with pytest.raises(ValueError):
        KeyValueStorage(worse_string_fixture)


def test_non_ascii_symbols_value_cannot_be_assigned(worst_string_fixture):
    """Testing that in case when value cannot be assigned to
     an attribute ValueError should is raised."""
    with pytest.raises(ValueError):
        KeyValueStorage(worst_string_fixture)


def test_builtin_value_cannot_be_assigned(builtin_key_fixture):
    """Testing that in case when value cannot be assigned to
     an attribute ValueError should is raised."""
    with pytest.raises(ValueError, match="value def cannot be "
                                         "assigned to an attribute"):
        KeyValueStorage(builtin_key_fixture)
