
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