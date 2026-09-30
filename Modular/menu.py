MENU = {
    1: {"name": "Burger", "price": 150.00, "category": "Main"},
    2: {"name": "Chicken Adobo", "price": 180.00, "category": "Main"},
    3: {"name": "Pancit Canton", "price": 120.00, "category": "Main"},
    4: {"name": "French Fries", "price": 80.00, "category": "Side"},
    5: {"name": "Lumpia", "price": 90.00, "category": "Side"},
    6: {"name": "Iced Tea", "price": 60.00, "category": "Drink"},
    7: {"name": "Mango Shake", "price": 95.00, "category": "Drink"},
}


# ---------- Menu functions ----------
def display_menu(menu):
    print("\n=== MENU ===")
    current = None
    for item_id, item in menu.items():
        if item["category"] != current:
            current = item["category"]
            print(f"\n-- {current} --")
        print(f"  {item_id}. {item['name']:<15} {CURRENCY}{item['price']:.2f}")
from config import CURRENCY