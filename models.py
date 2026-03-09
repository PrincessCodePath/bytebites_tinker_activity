# ByteBites: Customer, MenuItem, Menu, Order

class Customer:
    def __init__(self, name: str, purchase_history: list = None):
        self.name = name
        self.purchase_history = purchase_history or []

    def add_order(self, order: "Order"):
        self.purchase_history.append(order)


class MenuItem:
    def __init__(self, name: str, price: float, category: str, popularity_rating: int):
        self.name = name
        self.price = price
        self.category = category
        self.popularity_rating = popularity_rating


class Menu:
    def __init__(self, items: list = None):
        self.items = items or []

    def filter_by_category(self, category: str) -> list["MenuItem"]:
        return [i for i in self.items if i.category.lower() == category.lower()]

    def sort_by_price(self) -> list["MenuItem"]:
        return sorted(self.items, key=lambda i: i.price)

    def sort_by_popularity(self) -> list["MenuItem"]:
        return sorted(self.items, key=lambda i: i.popularity_rating, reverse=True)


class Order:
    def __init__(self, selected_items: list["MenuItem"] = None):
        self.selected_items = selected_items or []
        self.total_cost = sum(i.price for i in self.selected_items)

    def add_item(self, item: "MenuItem"):
        if not isinstance(item, MenuItem):
            raise ValueError("Item must be a MenuItem.")
        self.selected_items.append(item)
        self.total_cost += item.price

    def remove_item(self, item: "MenuItem"):
        if item in self.selected_items:
            self.selected_items.remove(item)
            self.total_cost -= item.price


if __name__ == "__main__":
    burger = MenuItem("Spicy Burger", 9.99, "Entrees", 8)
    soda = MenuItem("Large Soda", 2.49, "Drinks", 7)
    fries = MenuItem("Fries", 3.49, "Sides", 6)

    menu = Menu([burger, soda, fries])
    print("Filter Drinks:", [d.name for d in menu.filter_by_category("Drinks")])
    print("Sort by price:", [i.name for i in menu.sort_by_price()])
    print("Sort by popularity:", [i.name for i in menu.sort_by_popularity()])

    order = Order([burger, soda])
    print("Order total:", order.total_cost)
    order.add_item(fries)
    print("After add fries:", order.total_cost)

    cust = Customer("Alex")
    cust.add_order(order)
    print("Customer", cust.name, "orders:", len(cust.purchase_history))
