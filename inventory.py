class Inventory:
    def __init__(self):
        self.__inventory = []

    
    def add_product(self, prod):
        self.__inventory.append([prod.get_product_id(), prod.get_name(), prod.get_price(), prod.get_stock()])
        print("\nProduct added successfully!")


    def update_stock(self):
        print("\nUpdate Stock")
        idinp = input("Enter Product ID: ")
        for dict in self.__inventory:
            if idinp == dict["id"]:
                print(f"\nProduct Found:\nName: {dict['name']}\nCurrent Stock: {dict['stock']}\n")
                while True:
                    usrinp = input("New Stock Quantity: ")
                    try:
                        validn = int(usrinp)
                        dict["stock"] = validn
                        print("\nStock updated successfully!")
                        break
                    except ValueError:
                        print("Invalid Stock Quantity Entered! Try Again.")
        
        

    def search_product(self):
        found = False
        print("\nSearch Product")
        idinp = input("Enter Product ID: ")

        for dict in self.__inventory:
            if dict["id"] == idinp:
                print("\nProduct Found!")
                print("------------------------------------------------")
                print(f"ID: {dict['id']}\nName: {dict['name']}\nPrice: ${dict['price']}\nStock: {dict['stock']}")
                print("------------------------------------------------")
                found = True

        if not found:
            print("Product no found")
        
        return

    def display_all(self, inv):
        print("\nCurrent Inventory\n"
            "------------------------------------------------")
        for dict in inv:
            print(f"ID: {dict['id']} | Name: {dict['name']} | Price: ${dict['price']} | Stock: {dict['stock']}")
        print("------------------------------------------------")
        return


    def get_valid_input(self):
        while True:
            try:
                user = input("\nEnter option: ")
                value = int(user)
                if 1 <= value <= 6:
                    return value

                print("Number Out of range! Please choose options 1-6.")
            except ValueError:
                print("Invalid Option entered, please try again.")        

    