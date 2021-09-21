from homeworks.homework3.task3 import Filter, make_filter, sample_data


def test_to_catch_error_in_class_filter():
    """"""
    positive_even = Filter(lambda a: a % 2 == 0,
                           lambda a: a > 0,
                           lambda a: isinstance(a, int))
    error_cache = ''
    try:
        positive_even.apply(range(100))
    except TypeError:
        error_cache = 'error in class Filter - ' \
                      'use unpacking with __init__ func'
    assert error_cache == ''


def test_to_catch_errors_in_make_filter_func():
    """"""
    error_cache = ''
    try:
        make_filter(name='polly', type='bird').apply(sample_data)
    except TypeError:
        error_cache = 'error in make_filter func - ' \
                      'use unpacking with Filter class'
    assert error_cache == ''


def test_to_catch_errors_in_keyword_filter_func():
    """"""
    error_cache = ''
    if not make_filter(name='polly', type='bird').apply(sample_data):
        error_cache = 'error in keyword_filter_func - ' \
                      'expression "value[key]" does not give value'
    assert error_cache == ''
