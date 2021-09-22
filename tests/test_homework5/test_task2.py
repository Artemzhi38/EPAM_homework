from homeworks.homework5.task2 import custom_sum


# Positive tests
def test_decorated_function_works_with_two_params(capsys):
    """Testing that decorated original function works
    correctly with two arguments and give the result
    two times(first - for 'print' inside decorator and
    second - for 'return' in original function)"""
    assert custom_sum([1, 2, 3], [4, 5]) == [1, 2, 3, 4, 5]
    captured = capsys.readouterr()
    assert captured.out == "[1, 2, 3, 4, 5]\n"


def test_decorated_function_works_with_four_params(capsys):
    """Testing that decorated original function works
    correctly with four arguments"""
    assert custom_sum(1, 2, 3, 4) == 10
    captured = capsys.readouterr()
    assert captured.out == "10\n"


def test_original_function_docstring_is_callable():
    """Testing that decorated original function docstring
    is accessible with 'function.__doc__' command"""
    assert custom_sum.__doc__ == 'This function can sum any' \
                                 ' objects which have __add___'


def test_original_function_name_is_callable():
    """Testing that decorated original function name is
     accessible with 'function.__name__' command"""
    assert custom_sum.__name__ == 'custom_sum'


def test_original_function_is_callable():
    """Testing that original function is accessible with
     'function.__original_func' command"""
    assert callable(custom_sum.__original_func)


def test_called_original_function_works(capsys):
    """Testing that original function accessed with
    'function.__original_func' command does not print
     any output(gives result only once)"""
    assert custom_sum.__original_func(1, 2, 3, 4) == 10
    captured = capsys.readouterr()
    assert captured.out == ""
