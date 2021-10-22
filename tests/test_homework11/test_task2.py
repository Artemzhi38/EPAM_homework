from homeworks.homework11.task2 import Order, elder_discount, morning_discount


def test_default_example():
    """Testing that default example class
    instances work correctly"""
    order_1 = Order(100, morning_discount)
    assert order_1.final_price() == 75
    order_2 = Order(100, elder_discount)
    assert order_2.final_price() == 10


def test_new_discount():
    """Testing that new kind of discount can
    be added just with new function and does
    not involve modifying Order class"""
    def black_friday_discount(order):
        return order.price - order.price * -0.25

    order_3 = Order(100, black_friday_discount)
    assert order_3.final_price() == 125
