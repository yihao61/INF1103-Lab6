from product import Product
from inventory import Inventory

FILEPATH = "inventory.json"

def main():
    print("============================================================\n"
            "INVENTORY MANAGEMENT SYSTEM\n"
            "============================================================\n")

    inventory = Inventory(FILEPATH)
    inventory.load_inventory()
    exit_program = False

    print("\n----------- MENU -----------"
            "\n1. Display All Products"
            "\n2. Add Product"
            "\n3. Update Stock"
            "\n4. Search Product"
            "\n5. Save Inventory"
            "\n6. Exit"
            "\n----------------------------")

    while not exit_program:
        option = inventory.get_valid_input()
        match option:
            case 1:
                inventory.display_all(inventory)
            case 2:
                inventory = inventory.add_product(inventory)
            case 3:
                inventory.update_stock(inventory)
            case 4:
                inventory.search_product(inventory)
            case 5:
                inventory.save_inventory(inventory)
            case 6:
                exit_program = True

    inventory.save_inventory(inventory)
    print("Thank you for using Inventory Management System.")
    print("Program terminated.")



if __name__ == "__main__":
    main()