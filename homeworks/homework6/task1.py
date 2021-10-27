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
    setattr(cls, 'instance', 0)
    original_init = cls.__init__

    def __custom_init__(self, *args, **kwargs):
        """"Adds to original init-function incrementing of
        nonlocal instance variable value"""
        original_init(self, *args, **kwargs)
        cls.instance += 1
        setattr(self, 'get_created_instances', get_created_instances)
        setattr(self, 'reset_instances_counter', reset_instances_counter)

    def get_created_instances():
        """возвращает количество созданых экземпляров класса"""
        return cls.instance

    def reset_instances_counter():
        """сбрасывает счетчик экземпляров, возвращает значение до сброса"""
        value_before_reset = cls.instance
        cls.instance = 0
        return value_before_reset

    cls.__init__ = __custom_init__
    setattr(cls, 'get_created_instances', get_created_instances)
    setattr(cls, 'reset_instances_counter', reset_instances_counter)
    return cls
