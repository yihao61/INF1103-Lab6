class Inventory:
    def __init__(self, inventory=[]):
        self.__inventory = inventory

    def get_inventory(self):
        return self.__inventory

    def get_all_product_ids(self):
        all_ids = [product.get_product_id() for product in self.__inventory]
        return all_ids

    def add_product(self, prod):
        self.__inventory.append(prod)
        print("\nProduct added successfully!")
        return

    def update_stock(self):
        print("\nUpdate Stock")
        idinp = input("Enter Product ID: ")
        for prod in self.__inventory:
            if idinp == prod.get_product_id():
                print(f"\nProduct Found:\nName: {prod.get_name()}\nCurrent Stock: {prod.get_stock()}\n")
                while True:
                    usrinp = input("New Stock Quantity: ")
                    try:
                        validn = int(usrinp)
                        prod.update_stock(validn)
                        print("\nStock updated successfully!")
                        break
                    except ValueError:
                        print("Invalid Stock Quantity Entered! Try Again.")
        
        

    def search_product(self):
        found = False
        print("\nSearch Product")
        idinp = input("Enter Product ID: ")

        for prod in self.__inventory:
            if prod.get_product_id() == idinp:
                print("\nProduct Found!")
                print("------------------------------------------------")
                print(prod.display_information())
                print("------------------------------------------------")
                found = True

        if not found:
            print("Product not found")
        
        return

    def display_all(self):
        print("\nCurrent Inventory\n"
            "------------------------------------------------")
        for prod in self.__inventory:
            print(prod.display_information())
        print("------------------------------------------------")
        return


    

    