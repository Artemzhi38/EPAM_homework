from homeworks.homework3.task1 import cache


def test_for_one_time_cache():
    """Testing that function does not cache the result
    more than once if parameter "times" is set to 1"""
    @cache(times=1)
    def func(a, b):
        return (a ** b) ** 2
    some = 100, 200
    val_1 = func(*some)
    val_2 = func(*some)
    val_3 = func(*some)
    assert val_1 is val_2
    assert val_1 is not val_3


def test_for_disabling_cache():
    """Testing that function does not cache at all
    if parameter "times" is set to 0"""
    @cache(times=0)
    def func(a, b):
        return (a ** b) ** 2
    some = 100, 200
    val_1 = func(*some)
    val_2 = func(*some)
    assert val_1 is not val_2
