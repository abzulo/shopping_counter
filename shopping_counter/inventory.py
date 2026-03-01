# inventory.py
from shop_counter.data import products

# Fixed Product class
class Product:
    def __init__(self, pid, name, brand, category, price, stock, warranty):
        self.id = pid
        self.name = name
        self.brand = brand
        self.category = category
        self.price = price
        self.stock = stock
        self.warranty = warranty

    def reduce_stock(self, qty):
        if self.stock >= qty:
            self.stock -= qty
            return True
        return False


# Fixed Inventory class
class Inventory:
    def __init__(self):
        self.items = {
            name: Product(name=name, **details)
            for name, details in products.items()
        }

    def show_products(self):
        print("\nAvailable Products:")
        for item in self.items.values():
            print(
                f"{item.id} | {item.name} ({item.brand}) - "
                f"Category: {item.category} | Price: {item.price} KES | "
                f"Stock: {item.stock} | Warranty: {item.warranty}"
            )

    def update_stock(self, name, qty):
        if name in self.items:
            return self.items[name].reduce_stock(qty)
        return False