from homeworks.homework6.task1 import instances_counter


def test_get_created_instances_method_for_class_object():
    """Testing that method get_created_instances works,
    when called for decorated class"""
    @instances_counter
    class EmptyClass:
        pass
    assert EmptyClass.get_created_instances() == 0
    _ = EmptyClass(), EmptyClass(), EmptyClass()
    assert EmptyClass.get_created_instances() == 3


def test_get_created_instances_method_for_class_instance_object():
    """Testing that method get_created_instances works,
    when called for instance of decorated class"""
    @instances_counter
    class EmptyClass:
        pass
    obj1 = EmptyClass()
    assert obj1.get_created_instances() == 1


def test_reset_instances_counter_method_for_class_object():
    """Testing that method reset_instances_counter works,
    when called for decorated class"""
    @instances_counter
    class EmptyClass:
        pass
    _ = EmptyClass()
    assert EmptyClass.reset_instances_counter() == 1
    assert EmptyClass.get_created_instances() == 0


def test_reset_instances_counter_method_for_class_instance_object():
    """Testing that method reset_instances_counter works,
    when called for instance of decorated class"""
    @instances_counter
    class EmptyClass:
        pass
    obj1 = EmptyClass()
    assert obj1.reset_instances_counter() == 1
    assert obj1.get_created_instances() == 0


def test_get_created_instances_works_for_parent_and_child_classes():
    """Testing that method get_created_instances works
    separately, when called for decorated parent class
    and decorated child class"""
    @instances_counter
    class ParentClass:
        pass

    @instances_counter
    class ChildClass(ParentClass):
        pass

    _ = ParentClass(), ParentClass(), ChildClass()
    assert ParentClass.get_created_instances() == 3
    assert ChildClass.get_created_instances() == 1


def test_get_created_instances_works_for_instances_of_parent_and_child_cls():
    """Testing that method get_created_instances works
    separately, when called for instance of decorated
    parent class and instance of decorated child class"""
    @instances_counter
    class ParentClass:
        pass

    @instances_counter
    class ChildClass(ParentClass):
        pass

    obj1, _, obj3 = ParentClass(), ParentClass(), ChildClass()
    assert obj1.get_created_instances() == 3
    assert obj3.get_created_instances() == 1


def test_reset_instances_counter_for_parent_cls_do_not_affect_child_cls():
    """Testing that method reset_instances_counter
    applied for parent class does not affect instances
    of child class"""
    @instances_counter
    class ParentClass:
        pass

    @instances_counter
    class ChildClass(ParentClass):
        pass

    _ = ParentClass(), ParentClass(), ChildClass()
    assert ParentClass.reset_instances_counter() == 3
    assert ChildClass.get_created_instances() == 1


def test_reset_instances_counter_for_child_cls_do_not_affect_parent_cls():
    """Testing that method reset_instances_counter
    applied for child class does not affect instances
    of parent class"""
    @instances_counter
    class ParentClass:
        pass

    @instances_counter
    class ChildClass(ParentClass):
        pass

    _ = ParentClass(), ParentClass(), ChildClass()
    assert ChildClass.reset_instances_counter() == 1
    assert ParentClass.get_created_instances() == 3


def test_reset_instances_counter_for_parent_cls_instance_do_not_affect_child():
    """Testing that method reset_instances_counter
    applied for instance of parent class does not
    affect instances of child class"""
    @instances_counter
    class ParentClass:
        pass

    @instances_counter
    class ChildClass(ParentClass):
        pass

    obj1, _, obj3 = ParentClass(), ParentClass(), ChildClass()
    assert obj1.reset_instances_counter() == 3
    assert obj3.get_created_instances() == 1


def test_reset_instances_counter_for_child_cls_instance_do_not_affect_parent():
    """Testing that method reset_instances_counter
    applied for instance of child class does not
    affect instances of parent class"""
    @instances_counter
    class ParentClass:
        pass

    @instances_counter
    class ChildClass(ParentClass):
        pass

    obj1, _, obj3 = ParentClass(), ParentClass(), ChildClass()
    assert obj3.reset_instances_counter() == 1
    assert obj1.get_created_instances() == 3


def test_instances_counter_decorator_do_not_change_initialization():
    """Testing that decorator instances_counter does not
    change initialization process when applied to class
    that is parented by built-in 'list' class"""
    @instances_counter
    class CustomList(list):
        pass
    cl1 = CustomList('12345')
    cl2 = CustomList(['67', '89', '0'])
    cl3 = CustomList(('12345', '67890'))
    assert cl1 == ['1', '2', '3', '4', '5']
    assert cl2 == ['67', '89', '0']
    assert cl3 == ['12345', '67890']
