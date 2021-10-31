from homeworks.homework11.task1 import SimplifiedEnum


def test_two_default_classes():
    """Testing that metaclass is working properly
     with default examples"""
    class ColorsEnum(metaclass=SimplifiedEnum):
        __keys = ("RED", "BLUE", "ORANGE", "BLACK")

    class SizesEnum(metaclass=SimplifiedEnum):
        __keys = ("XL", "L", "M", "S", "XS")
    assert ColorsEnum.RED == "RED"
    assert SizesEnum.XL == "XL"


def test_subclass_has_attrs_of_parent_class():
    """Testing that child class has all the attrs
     of custom-metaclass based parent class"""
    class ColorsEnum(metaclass=SimplifiedEnum):
        __keys = ("RED", "BLUE", "ORANGE", "BLACK")

    class ChildColorsEnum(ColorsEnum):
        pass
    assert ChildColorsEnum.RED == "RED"


def test_subclass_has_own_attrs_and_attrs_of_parent_class():
    """Testing that custom-metaclass based child class has all the attrs
     of custom-metaclass based parent class and has his own attrs
     implemented through custom metaclass"""
    class ColorsEnum(metaclass=SimplifiedEnum):
        __keys = ("RED", "BLUE", "ORANGE", "BLACK")

    class ChildColorsEnum(ColorsEnum, metaclass=SimplifiedEnum):
        __keys = ("GREEN", "WHITE", "BLACK", "YELLOW")
    assert ChildColorsEnum.RED == "RED"
    assert ChildColorsEnum.GREEN == "GREEN"
