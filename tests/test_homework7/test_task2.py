from homeworks.homework7.task2 import backspace_compare


def test_default_examples():
    """Testing that function works right
    with three default examples"""
    assert backspace_compare("ab#c", "ad#c")
    assert backspace_compare("a##c", "#a#c")
    assert not backspace_compare("a#c", "b")


def test_only_backspace_chars():
    """Testing that function works right
    when both strings consist only of '#'
    chars and have different lengths"""
    assert backspace_compare("#####", "#")


def test_no_backspace_chars():
    """Testing that function works right
    when both strings do not have any '#'
    chars"""
    assert backspace_compare("abc", "abc")
    assert not backspace_compare("abc", "abcd")


def test_complex_input_strings():
    """Testing that function works right
    with some complex strings"""
    assert backspace_compare("a#b##c###", "#")
    assert backspace_compare("""abc012##
####c#c""", "###ac")
