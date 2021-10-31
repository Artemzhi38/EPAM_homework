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
"""
import functools


def custom_wraps(orig_func):

    def custom_update_wrapper(wrapper):
        wrapper.__name__ = orig_func.__name__
        wrapper.__doc__ = orig_func.__doc__
        wrapper.__original_func = orig_func
        return wrapper

    return custom_update_wrapper


def print_result(func):
    @custom_wraps(func)
    def wrapper(*args, **kwargs):
        """Function-wrapper which print result of an original function"""
        result = func(*args, **kwargs)
        print(result)
        return result

    return wrapper


def custom_sum(*args):
    """This function can sum any objects which have __add___"""
    return functools.reduce(lambda x, y: x + y, args)
