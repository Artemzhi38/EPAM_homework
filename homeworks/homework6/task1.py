"""
Написать декоратор instances_counter, который применяется к любому классу
и добавляет ему 2 метода:
get_created_instances - возвращает количество созданых экземпляров класса
reset_instances_counter - сбросить счетчик экземпляров,
возвращает значение до сброса
Имя декоратора и методов не менять
Ниже пример использования
"""


def instances_counter(cls):
    """Decorates any class with get_created_instances
    and reset_instances_counter methods"""
    instance = 0
    original_init = cls.__init__

    def __custom_init__(*args, **kwargs):
        """"Adds to original init-function incrementing of
        nonlocal instance variable value"""
        original_init(*args, **kwargs)
        nonlocal instance
        instance += 1

    def get_created_instances(_=None):
        """возвращает количество созданых экземпляров класса"""
        nonlocal instance
        return instance

    def reset_instances_counter(_=None):
        """сбрасывает счетчик экземпляров, возвращает значение до сброса"""
        nonlocal instance
        value_before_reset = instance
        instance = 0
        return value_before_reset

    cls.__init__ = __custom_init__
    cls.get_created_instances = get_created_instances
    cls.reset_instances_counter = reset_instances_counter

    return cls
