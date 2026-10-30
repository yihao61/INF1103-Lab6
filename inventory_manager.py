from product import Product
from inventory import Inventory
from FileHandling import save_inventory, load_inventory

FILEPATH = "inventory.json"

def get_valid_input():
    while True:
        try:
            user = input("\nEnter option: ")
            if user.lower() == "exit":
                print("Exiting program...")
                return 6
            
            value = int(user)
            if 1 <= value <= 6:
                return value

            print("Number Out of range! Please choose options 1-6.")
        except ValueError:
            print("Invalid Option entered, please try again.")        

def main():
    print("============================================================\n"
            "INVENTORY MANAGEMENT SYSTEM\n"
            "============================================================\n")

    inventory = Inventory(load_inventory(FILEPATH))
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
        option = get_valid_input()
        match option:
            case 1:
                inventory.display_all()
            case 2:
                Adding = True
                progress = 0
                newprod = {}
                print("Add New Product")
                while Adding:
                    if progress == 0:
                        idinp = input("Product ID: ")
                        if idinp in inventory.get_all_product_ids():                
                            print("ID already exits. Please pick a new one.")
                            continue
            
                        newprod["id"] = idinp
                        progress+=1
            
                    elif progress == 1:
                        nameinp = input("Product Name: ")
                        newprod["name"] = nameinp
                        progress+=1
            
                    elif progress == 2:
                        priceinp = input("Price: ")
                        try:
                            validp = float(priceinp)
                        except ValueError:
                            print("Not a number. Try Again")
                            continue
                
                        newprod["price"] = validp
                        progress+=1
            
                    elif progress == 3:
                        stockinp = input("Stock Quantity: ")
            
                        try:
                            valids = int(stockinp)
                        except ValueError:
                            print("Not a integer. Try Again!")
                            continue
                
                        newprod["stock"] = valids
                        progress+=1
                    else:
                        Adding = False

                inventory.add_product(Product(**newprod))
                
            case 3:
                inventory.update_stock()
            case 4:
                inventory.search_product()
            case 5:
                save_inventory(inventory.get_inventory(), FILEPATH)
            case 6:
                exit_program = True

    save_inventory(inventory.get_inventory(), FILEPATH)
    print("Thank you for using Inventory Management System.")
    print("Program terminated.")



if __name__ == "__main__":
    main()