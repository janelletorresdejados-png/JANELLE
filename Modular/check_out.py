def checkout(order, menu):
    if not order:
        print("Nothing to check out.")
        return False
    view_order(order, menu)
    _, _, total = calculate_totals(order, menu)
    while True:
        payment = read_float(f"\nEnter payment amount (total {CURRENCY}{total:.2f}): ")
        if payment is None:
            print("Please enter a valid number.")
        elif payment < total:
            print("Insufficient payment.")
        else:
            print_receipt(order, menu, payment)
            return True
from display import view_order, print_receipt
from order import calculate_totals
from input import read_float