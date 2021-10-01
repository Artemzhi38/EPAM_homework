from homeworks.homework5.task2 import custom_sum, print_result


# Positive tests
def test_decorated_function_works_with_two_params():
    """Testing that decorated original function works
    correctly with two arguments"""
    original_custom_sum = custom_sum
    decorated_custom_sum = print_result(custom_sum)
    assert original_custom_sum([1, 2, 3], [4, 5]) == \
           decorated_custom_sum([1, 2, 3], [4, 5])


def test_decorated_function_works_with_four_params():
    """Testing that decorated original function works
    correctly with four arguments"""
    original_custom_sum = custom_sum
    decorated_custom_sum = print_result(custom_sum)
    assert original_custom_sum(1, 2, 3, 4) == \
           decorated_custom_sum(1, 2, 3, 4)


def test_original_function_docstring_is_callable():
    """Testing that decorated original function docstring
    is accessible with 'function.__doc__' command"""
    original_custom_sum = custom_sum
    decorated_custom_sum = print_result(custom_sum)
    assert original_custom_sum.__doc__ == \
        decorated_custom_sum.__doc__


def test_original_function_name_is_callable():
    """Testing that decorated original function name is
     accessible with 'function.__name__' command"""
    original_custom_sum = custom_sum
    decorated_custom_sum = print_result(custom_sum)
    assert original_custom_sum.__name__ == \
           decorated_custom_sum.__name__


def test_original_function_is_callable():
    """Testing that original function is accessible from
    decorated function with 'function.__original_func' command"""
    original_custom_sum = custom_sum
    decorated_custom_sum = print_result(custom_sum)
    assert decorated_custom_sum.__original_func == original_custom_sum
