from menu import MENU, display_menu
from order import add_to_order, remove_from_order
from display import view_order
from check_out import checkout
from input import read_int


def show_options():
    print("\n[1] View menu  [2] Add item  [3] Remove item")
    print("[4] View order [5] Checkout  [0] Exit")


def main():
    order = {}
    print("Welcome to Python Bistro!")
    while True:
        show_options()
        choice = input("Choose: ").strip()

        if choice == "1":
            display_menu(MENU)
        elif choice == "2":
            display_menu(MENU)
            item_id = read_int("Item number: ")
            qty = read_int("Quantity: ")
            if item_id is None or qty is None:
                print("Invalid input.")
            else:
                print(add_to_order(order, MENU, item_id, qty)[1])
        elif choice == "3":
            view_order(order, MENU)
            item_id = read_int("Item number to remove: ")
            qty = read_int("Quantity to remove: ")
            if item_id is None or qty is None:
                print("Invalid input.")
            else:
                print(remove_from_order(order, MENU, item_id, qty)[1])
        elif choice == "4":
            view_order(order, MENU)
        elif choice == "5":
            if checkout(order, MENU):
                order.clear()
        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()