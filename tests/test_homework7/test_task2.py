import pytest

from homeworks.homework7.task2 import backspace_compare


# positive tests
@pytest.mark.parametrize("test_input", [("ab#c", "ad#c"), ("a##c", "#a#c"),
                                        ("#####", "#"), ("a#b##c###", "#"),
                                        ("""abc012#####c#c""", "###ac"),
                                        ("abc", "abc")])
def test_default_examples(test_input):
    """Testing that function returns True in cases of:
    - default examples
    - both strings consist only of '#'
    chars and have different lengths
    - some complex strings examples"""
    assert backspace_compare(*test_input)


# negative tests
@pytest.mark.parametrize("test_input", [("abc", "abcd"), ("a#c", "b")])
def test_complex_input_strings(test_input):
    """Testing that function returns false when given
     different(after backspacing) strings"""
    assert not backspace_compare(*test_input)
