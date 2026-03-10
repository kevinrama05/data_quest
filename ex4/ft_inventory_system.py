from sys import argv

if __name__ == "__main__":
    inventory = {}
    for i in range(1, len(argv)):
        try:
            item, quantity = argv[i].split(":")
        except ValueError:
            pass
        else:
            try:
                inventory[item] = int(quantity)
            except ValueError:
                pass
    print("=== Inventory System Analytics ===")
    total = 0
    for i in inventory.values():
        total += i
    print(f"Total items in inventory: {total}")
    print(f"Unique item types: {len(inventory)}")

    print("\n=== Current Inventory ===")
    for item, quantity in inventory.items():
        print(f"{item}: {quantity} units ({(quantity / total * 100):.2f})")

    print("\n=== Inventory Statistics ===")
    print(f"Most abundant: {max(inventory, key=inventory.get)} ({inventory[max(inventory, key=inventory.get)]} units)")
    print(f"Least abundant: {min(inventory, key=inventory.get)} ({inventory[min(inventory, key=inventory.get)]} units)")

    moderate = {k: v for k, v in inventory.items() if v >= 5}
    scarce = {k: v for k, v in inventory.items() if v <= 1}

    print("\n=== Item Categories ===")
    print(f"Moderate:  {moderate}")
    print(f"Scarce:  {scarce}")

    restock = [k for k, v in inventory.items() if v <= 1]

    print("\n=== Management Suggestions ===")
    print(f"• Restock needed:  {restock}")

    print("\n=== Dictionary Properties Demo ===")
    print(f"Dictionary keys:  {list(inventory.keys())}")
    print(f"Dictionary values:  {list(inventory.values())}")
    print(f"Sample lookup - 'sword' in inventory:  {'sword' in inventory}")
