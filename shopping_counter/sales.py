# sales.py

from shopping_counter.inventory import Inventory
import json


class Sale:
    def __init__(self, item, qty, total):
        self.item = item
        self.qty = qty
        self.total = total
        self.inventory = Inventory()

    def process(self):
        """
        Attempt to reduce stock before saving sale
        """
        success = self.inventory.update_stock(self.item, self.qty)

        if success:
            self.save()
            print("Sale recorded successfully.")
        else:
            print("Sale failed: Not enough stock available.")

    def save(self):
        sale = {
            "item": self.item,
            "quantity": self.qty,
            "total": self.total
        }

        with open("sales_history.json", "a") as f:
            f.write(json.dumps(sale) + "\n") 