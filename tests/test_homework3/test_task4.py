from homeworks.homework3.task4 import is_armstrong


def test_positive_case():
    """Testing that function given an
    Armstrong number gives True"""
    assert is_armstrong(153) is True


def test_negative_case():
    """Testing that function given not an
    Armstrong number gives False"""
    assert is_armstrong(10) is False
