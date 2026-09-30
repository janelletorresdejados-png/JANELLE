from config import TAX_RATE
def add_to_order(order, menu, item_id, qty):
    if item_id not in menu:
        return False, "Invalid item number."
    if qty <= 0:
        return False, "Quantity must be at least 1."
    order[item_id] = order.get(item_id, 0) + qty
    return True, f"Added {qty} x {menu[item_id]['name']}."


def remove_from_order(order, menu, item_id, qty):
    if item_id not in order:
        return False, "That item is not in your order."
    if qty <= 0:
        return False, "Quantity must be at least 1."
    order[item_id] -= qty
    if order[item_id] <= 0:
        del order[item_id]
    return True, f"Removed from {menu[item_id]['name']}."


def calculate_subtotal(order, menu):
    return sum(menu[i]["price"] * q for i, q in order.items())


def calculate_totals(order, menu, tax_rate=TAX_RATE):
    subtotal = calculate_subtotal(order, menu)
    tax = subtotal * tax_rate
    return subtotal, tax, subtotal + tax
