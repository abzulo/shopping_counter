import argparse
from shopping_counter.inventory import Inventory
from shopping_counter.sales import Sale


def main():
    parser = argparse.ArgumentParser(description="Shop Counter CLI")
    parser.add_argument("command", choices=["show", "buy", "history"], help="Action to perform")
    parser.add_argument("--item", help="Product name (for buy)")
    parser.add_argument("--qty", type=int, help="Quantity (for buy)")
    args = parser.parse_args()

    inv = Inventory()

    if args.command == "show":
        inv.show_products()
    elif args.command == "buy":
        if inv.update_stock(args.item, args.qty):
            total = inv.items[args.item].price * args.qty
            sale = Sale(args.item, args.qty, total)
            sale.save()
            print(f"✅ Bought {args.qty} {args.item}(s) for {total} KES.")
        else:
            print("❌ Not enough stock or item not found.")
    elif args.command == "history":
        try:
            with open("sales_history.json", "r") as f:
                print("\n--- Past Sales ---")
                for line in f:
                    print(line.strip())
        except FileNotFoundError:
            print("No past sales found.")

if __name__ == "__main__":
    main()