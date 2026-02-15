store_inventory = {}


def add_product(inventory, product_name, quantity):
    """Used to add a product and quantity to the inventory."""
    inventory = store_inventory
    inventory[product_name] = quantity


def remove_product(inventory, product_name):
    """Used to completely remove a product from the inventory."""
    inventory = store_inventory
    if product_name in inventory:
        inventory.pop(product_name)
        print(f"\n{product_name} removed from inventory.\n")
    else:
        print("\nProduct not in inventory.\n")


def update_quantity(inventory, product_name, new_quantity):
    """Used to add items to inventory."""
    inventory = store_inventory
    if product_name in inventory:
        inventory[product_name] += int(new_quantity)
        print(f"\nNew quantity: {inventory[product_name]}\n")
    else:
        print("\nProduct not in inventory.\n")


def check_stock(inventory, product_name):
    """Used to check current stock of a product."""
    inventory = store_inventory
    print(f"\n{product_name} current stock is {inventory.get(product_name)}.\n")


def show_inventory(inventory):
    """Used to display the whole inventory."""
    inventory = store_inventory
    print("\n---Store Inventory---")
    for key, value in inventory.items():
        print(f"- {key}: {value}\n\n")


print("Running inventory manager...")

# Inventory Loop
while True:
    print(
        "Commands: \nadd - add a product \nremove - remove a product \nupdateq - update quantity"
        "\nstock - check stock for product \nshow - show current inventory"
    )
    choice = input("Command: ")

    if choice == "add":  # command used to add a product to the store inventory
        choice_add_quantity = int
        choice_add_product = input("Product name: ")
        choice_add_quantity = int(input("Quantity: "))
        add_product(
            inventory="", product_name=choice_add_product, quantity=choice_add_quantity
        )
        print("\nProduct added successfully!\n")
        print(store_inventory)
        continue

    elif (
        choice == "remove"
    ):  # command used to remove a product from the store inventory
        choice_remove_product = input("Product to remove: ")
        remove_product(inventory="", product_name=choice_remove_product)
        print(store_inventory)
        continue

    elif choice == "updateq":  # command used to update quantity of a product
        choice_update_product = input("Product name: ")
        choice_update_quantity = int(input("Insert quantity: "))
        update_quantity(
            inventory="",
            product_name=choice_update_product,
            new_quantity=choice_update_quantity,
        )
        print(store_inventory)
        continue

    elif choice == "stock":  # command used to show current stock
        choice_get_stock = input("Product: ")
        check_stock(inventory="", product_name=choice_get_stock)
        continue

    elif choice == "show":  # command used to print the whole inventory
        show_inventory(inventory="")
        continue

    else:
        print("\nI don't recognize that command.\n")
        continue
