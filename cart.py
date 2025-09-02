import items
import billing
import receipt

cart = []

def start_shopping():
    while True:
        print("\nAvailable items:")
        for code, (name, price, stock) in items.prices.items():
            print(f"{code}: {name} - Rs.{price} (Stock: {stock})")

        choice = input("\nEnter 'add' to add item, 'remove' to remove item, or 'done' to finish: ").lower()

        if choice == "done
