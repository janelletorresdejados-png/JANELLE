from itertools import count


class MenuItem:
    def __init__(self, item_id, name, price, category):
        self.item_id = item_id
        self.name = name
        self.price = price
        self.category = category

    def __str__(self):
        return f"{self.item_id}. {self.name:<15} ₱{self.price:.2f}"


class Menu:
    def __init__(self):
        self._items = {}

    def add_item(self, item):
        self._items[item.item_id] = item

    def get_item(self, item_id):
        return self._items.get(item_id)

    def display(self):
        print("\n=== MENU ===")
        current = None
        for item in self._items.values():
            if item.category != current:
                current = item.category
                print(f"\n-- {current} --")
            print(f"  {item}")


class OrderLine:
    def __init__(self, menu_item, quantity):
        self.menu_item = menu_item
        self.quantity = quantity

    @property
    def total(self):
        return self.menu_item.price * self.quantity

    def __str__(self):
        return f"{self.quantity} x {self.menu_item.name:<15} ₱{self.total:.2f}"


class Order:
    TAX_RATE = 0.12
    _ids = count(1)

    def __init__(self):
        self.order_id = next(Order._ids)
        self._lines = {}
        self.paid = False

    def is_empty(self):
        return not self._lines

    def add(self, menu_item, quantity):
        if quantity <= 0:
            raise ValueError("Quantity must be at least 1.")
        if menu_item.item_id in self._lines:
            self._lines[menu_item.item_id].quantity += quantity
        else:
            self._lines[menu_item.item_id] = OrderLine(menu_item, quantity)

    def remove(self, item_id, quantity):
        if item_id not in self._lines:
            raise KeyError("That item is not in your order.")
        if quantity <= 0:
            raise ValueError("Quantity must be at least 1.")
        line = self._lines[item_id]
        line.quantity -= quantity
        if line.quantity <= 0:
            del self._lines[item_id]

    @property
    def subtotal(self):
        return sum(line.total for line in self._lines.values())

    @property
    def tax(self):
        return self.subtotal * self.TAX_RATE

    @property
    def total(self):
        return self.subtotal + self.tax

    def display(self):
        if self.is_empty():
            print("\nYour order is empty.")
            return
        print(f"\n=== ORDER #{self.order_id} ===")
        for line in self._lines.values():
            print(f"  {line}")
        print(f"\n  Subtotal: ₱{self.subtotal:.2f}")
        print(f"  Tax ({self.TAX_RATE:.0%}): ₱{self.tax:.2f}")
        print(f"  TOTAL:    ₱{self.total:.2f}")

    def lines(self):
        return list(self._lines.values())


class Receipt:
    def __init__(self, order, payment):
        self.order = order
        self.payment = payment

    def print(self):
        o = self.order
        print("\n" + "=" * 32)
        print(f"     RECEIPT - ORDER #{o.order_id}")
        print("=" * 32)
        for line in o.lines():
            print(f"{line.quantity} x {line.menu_item.name:<15}₱{line.total:>8.2f}")
        print("-" * 32)
        print(f"{'Subtotal':<18}₱{o.subtotal:>8.2f}")
        print(f"{'Tax':<18}₱{o.tax:>8.2f}")
        print(f"{'Total':<18}₱{o.total:>8.2f}")
        print(f"{'Paid':<18}₱{self.payment:>8.2f}")
        print(f"{'Change':<18}₱{self.payment - o.total:>8.2f}")
        print("=" * 32)
        print("  Thank you! Come again!")


class Restaurant:
    def __init__(self, name):
        self.name = name
        self.menu = Menu()
        self.current_order = Order()
        self.completed_orders = []
        self._load_menu()

    def _load_menu(self):
        data = [
            (1, "Burger", 150, "Main"),
            (2, "Chicken Adobo", 180, "Main"),
            (3, "Pancit Canton", 120, "Main"),
            (4, "French Fries", 80, "Side"),
            (5, "Lumpia", 90, "Side"),
            (6, "Iced Tea", 60, "Drink"),
            (7, "Mango Shake", 95, "Drink"),
        ]
        for item in data:
            self.menu.add_item(MenuItem(*item))

    def add_item(self):
        self.menu.display()
        item = self.menu.get_item(self._read_int("Item number: "))
        if item is None:
            print("Invalid item number.")
            return
        try:
            qty = self._read_int("Quantity: ")
            self.current_order.add(item, qty)
            print(f"Added {qty} x {item.name}.")
        except ValueError as e:
            print(e)

    def remove_item(self):
        self.current_order.display()
        try:
            item_id = self._read_int("Item number to remove: ")
            qty = self._read_int("Quantity to remove: ")
            self.current_order.remove(item_id, qty)
            print("Order updated.")
        except (ValueError, KeyError) as e:
            print(e.args[0])

    def checkout(self):
        order = self.current_order
        if order.is_empty():
            print("Nothing to check out.")
            return
        order.display()
        while True:
            try:
                payment = float(input(f"\nEnter payment (total ₱{order.total:.2f}): "))
            except ValueError:
                print("Please enter a valid number.")
                continue
            if payment < order.total:
                print("Insufficient payment.")
                continue
            Receipt(order, payment).print()
            order.paid = True
            self.completed_orders.append(order)
            self.current_order = Order()
            return

    @staticmethod
    def _read_int(prompt):
        try:
            return int(input(prompt))
        except ValueError:
            raise ValueError("Please enter a valid number.")

    def run(self):
        print(f"Welcome to {self.name}!")
        while True:
            print("\n[1] View menu  [2] Add item  [3] Remove item")
            print("[4] View order [5] Checkout  [0] Exit")
            choice = input("Choose: ").strip()
            try:
                if choice == "1":
                    self.menu.display()
                elif choice == "2":
                    self.add_item()
                elif choice == "3":
                    self.remove_item()
                elif choice == "4":
                    self.current_order.display()
                elif choice == "5":
                    self.checkout()
                elif choice == "0":
                    print("Goodbye!")
                    break
                else:
                    print("Invalid choice.")
            except ValueError as e:
                print(e)


if __name__ == "__main__":
    Restaurant("Python Bistro").run()