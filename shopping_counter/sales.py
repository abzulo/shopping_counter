from shop_counter.inventory import update_stock
from shop_counter.data import products
import json


class Sale:
    def __init__(self, item, qty, total):
        self.item = item
        self.qty = qty
        self.total = total

    def save(self):
        sale = {"item": self.item, "quantity": self.qty, "total": self.total}
        with open("sales_history.json", "a") as f:
            f.write(json.dumps(sale) + "\n")

def buy_item(item, quantity):
    if update_stock(item, quantity):
        total = products[item]["price"] * quantity
        print(f"✅ You bought {quantity} {item}(s) for {total} KES.")
       
        sale = Sale(item, quantity, total)
        sale.save()
    else:
        print("❌ Not enough stock or item not found.")