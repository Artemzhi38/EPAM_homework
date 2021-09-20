"""
Написать декоратор который позволит сохранять информацию из
исходной функции (__name__ and __doc__), а так же сохранит саму
исходную функцию в атрибуте __original_func
print_result изменять нельзя, за исключением добавления вашего
декоратора на строку отведенную под него - замените комментарий
До применения вашего декоратор будет вызываться AttributeError
при custom_sum.__original_func
Это корректное поведение
После применения там должна быть исходная функция
Ожидаемый результат:
print(custom_sum.__doc__)  # 'This function can sum any objects
 which have __add___'
print(custom_sum.__name__)  # 'custom_sum'
print(custom_sum.__original_func)  # <function custom_sum at
<some_id>>

Doctests for custom_wraps decorator:
#to run them use 'pytest --doctest-modules' command

# Positive tests

# Testing that decorated original function works correctly with
# two arguments and give the result two times (first - for 'print'
# inside decorator and second - for 'return' in original function)
>>> custom_sum([1, 2, 3], [4, 5])
[1, 2, 3, 4, 5]
[1, 2, 3, 4, 5]

# Testing that decorated original function works correctly with
# four arguments
>>> custom_sum(1, 2, 3, 4)
10
10

# Testing that decorated original function docstring is accessible
# with 'function.__doc__' command
>>> custom_sum.__doc__
'This function can sum any objects which have __add___'

# Testing that decorated original function name is accessible with
# 'function.__name__' command
>>> custom_sum.__name__
'custom_sum'

# Testing that original function is accessible with
# 'function.__original_func' command
>>> custom_sum.__original_func
<function custom_sum at ...>

# Testing that original function accessed with
# 'function.__original_func' command does not print
# any output(gives result only once)
>>> custom_sum.__original_func(1, 2, 3, 4)
10

"""
import functools


def custom_wraps(orig_func):

    def custom_update_wrapper(wrapper, wrapped):
        wrapper.__name__ = wrapped.__name__
        wrapper.__doc__ = wrapped.__doc__
        wrapper.__original_func = wrapped
        return wrapper

    return functools.partial(custom_update_wrapper, wrapped=orig_func)


def print_result(func):
    @custom_wraps(func)
    def wrapper(*args, **kwargs):
        """Function-wrapper which print result of an original function"""
        result = func(*args, **kwargs)
        print(result)
        return result

    return wrapper


@print_result
def custom_sum(*args):
    """This function can sum any objects which have __add___"""
    return functools.reduce(lambda x, y: x + y, args)


if __name__ == "__main__":
    custom_sum([1, 2, 3], [4, 5])
    custom_sum(1, 2, 3, 4)

    print(custom_sum.__doc__)
    print(custom_sum.__name__)
    without_print = custom_sum.__original_func

    # the result returns without printing
    without_print(1, 2, 3, 4)
