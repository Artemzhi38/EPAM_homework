import pytest
from homeworks.homework9.task2 import SupressorCls, supressor_gen


# Tests for class context manager
def test_class_context_manager_index_error():
    """"""
    with pytest.raises(IndexError):
        [][2]
    with SupressorCls(IndexError):
        [][2]
    with pytest.raises(IndexError):
        [][2]


def test_class_context_manager_zero_division_error():
    """"""
    with pytest.raises(ZeroDivisionError):
        1/0
    with SupressorCls(ZeroDivisionError):
        1/0
    with pytest.raises(ZeroDivisionError):
        1/0


def test_class_context_manager_not_supressed_error():
    """"""
    with pytest.raises(ZeroDivisionError):
        with SupressorCls(ValueError):
            1/0


# Tests for generator context manager
def test_generator_context_manager_index_error():
    """"""
    with pytest.raises(IndexError):
        [][2]
    with supressor_gen(IndexError):
        [][2]
    with pytest.raises(IndexError):
        [][2]


def test_generator_context_manager_zero_division_error():
    """"""
    with pytest.raises(ZeroDivisionError):
        1/0
    with supressor_gen(ZeroDivisionError):
        1/0
    with pytest.raises(ZeroDivisionError):
        1/0


def test_generator_context_manager_not_supressed_error():
    """"""
    with pytest.raises(ZeroDivisionError):
        with supressor_gen(ValueError):
            1/0
