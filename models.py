# ByteBites models: Customer, MenuItem, Menu, Order

class Customer:
    def __init__(self, name: str, purchase_history: list["Order"] = None):
        self.name = name
        self.purchase_history = purchase_history if purchase_history is not None else []

    def add_order(self, order: "Order"):
        """Adds an order to the customer's purchase history."""
        self.purchase_history.append(order)


class MenuItem:
    def __init__(self, name: str, price: float, category: str, popularity_rating: int):
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Name must be a non-empty string.")
        if not isinstance(price, (int, float)) or price <= 0:
            raise ValueError("Price must be a positive number.")
        if not isinstance(category, str) or not category.strip():
            raise ValueError("Category must be a non-empty string.")
        if not isinstance(popularity_rating, int) or popularity_rating < 0:
            raise ValueError("Popularity rating must be a non-negative integer.")

        self.name = name
        self.price = price
        self.category = category
        self.popularity_rating = popularity_rating


class Menu:
    def __init__(self, items: list["MenuItem"] = None):
        if items is not None and not all(isinstance(item, MenuItem) for item in items):
            raise ValueError("All items must be instances of MenuItem.")
        self.items = items if items is not None else []

    def filter_by_category(self, category: str) -> list["MenuItem"]:
        """Filters the menu items by the given category."""
        return [item for item in self.items if item.category == category]


class Order:
    def __init__(self, selected_items: list["MenuItem"] = None):
        if selected_items is not None and not all(isinstance(item, MenuItem) for item in selected_items):
            raise ValueError("All selected items must be instances of MenuItem.")
        self.selected_items = selected_items if selected_items is not None else []
        self.total_cost = self._calculate_total()

    def _calculate_total(self) -> float:
        """Calculates the total cost of the order."""
        return sum(item.price for item in self.selected_items)

    def add_item(self, item: "MenuItem"):
        """Adds an item to the order and updates the total cost."""
        if not isinstance(item, MenuItem):
            raise ValueError("Item must be an instance of MenuItem.")
        self.selected_items.append(item)
        self.total_cost = self._calculate_total()

    def remove_item(self, item: "MenuItem"):
        """Removes an item from the order and updates the total cost."""
        if item in self.selected_items:
            self.selected_items.remove(item)
            self.total_cost = self._calculate_total()


if __name__ == "__main__":
    # quick manual check (Part 2e)
    burger = MenuItem("Spicy Burger", 9.99, "Entrees", 8)
    soda = MenuItem("Large Soda", 2.49, "Drinks", 7)
    print("MenuItem:", burger.name, burger.price, burger.category, burger.popularity_rating)

    menu = Menu([burger, soda])
    drinks = menu.filter_by_category("Drinks")
    print("Filter Drinks:", [d.name for d in drinks])

    order = Order([burger, soda])
    print("Order total:", order.total_cost, "items:", [i.name for i in order.selected_items])

    cust = Customer("Alex", [])
    cust.add_order(order)
    print("Customer:", cust.name, "history len:", len(cust.purchase_history))
