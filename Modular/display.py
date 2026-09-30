def view_order(order, menu):
    if not order:
        print("\nYour order is empty.")
        return
    print("\n=== YOUR ORDER ===")
    for item_id, qty in order.items():
        item = menu[item_id]
        print(f"  {qty} x {item['name']:<15} {CURRENCY}{item['price'] * qty:.2f}")
    subtotal, tax, total = calculate_totals(order, menu)
    print(f"\n  Subtotal: {CURRENCY}{subtotal:.2f}")
    print(f"  Tax ({TAX_RATE:.0%}): {CURRENCY}{tax:.2f}")
    print(f"  TOTAL:    {CURRENCY}{total:.2f}")


def print_receipt(order, menu, payment):
    subtotal, tax, total = calculate_totals(order, menu)
    print("\n" + "=" * 32)
    print("          RECEIPT")
    print("=" * 32)
    for item_id, qty in order.items():
        item = menu[item_id]
        print(f"{qty} x {item['name']:<15}{CURRENCY}{item['price'] * qty:>8.2f}")
    print("-" * 32)
    print(f"{'Subtotal':<18}{CURRENCY}{subtotal:>8.2f}")
    print(f"{'Tax':<18}{CURRENCY}{tax:>8.2f}")
    print(f"{'Total':<18}{CURRENCY}{total:>8.2f}")
    print(f"{'Paid':<18}{CURRENCY}{payment:>8.2f}")
    print(f"{'Change':<18}{CURRENCY}{payment - total:>8.2f}")
    print("=" * 32)
    print("  Thank you! Come again!")

from config import CURRENCY, TAX_RATE
from order import calculate_totals