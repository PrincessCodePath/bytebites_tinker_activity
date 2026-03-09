from models import Customer, MenuItem, Menu, Order


def test_order_total_with_items():
    burger = MenuItem("Spicy Burger", 9.99, "Entrees", 8)
    soda = MenuItem("Large Soda", 2.49, "Drinks", 7)
    order = Order([burger, soda])
    assert order.total_cost == 12.48


def test_empty_order_total():
    order = Order()
    assert order.total_cost == 0


def test_filter_by_category_drinks():
    burger = MenuItem("Spicy Burger", 9.99, "Entrees", 8)
    soda = MenuItem("Large Soda", 2.49, "Drinks", 7)
    fries = MenuItem("Fries", 3.49, "Sides", 6)
    menu = Menu([burger, soda, fries])
    drinks = menu.filter_by_category("Drinks")
    assert len(drinks) == 1
    assert drinks[0].name == "Large Soda"
