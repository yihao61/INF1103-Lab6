class Product:
    def __init__(self, id, name, price, stock):
        self.__product_id = id
        self.__name = name
        self.__price = price
        self.__stock = stock

    def update_stock(self, quantity):
        if quantity >= 0: 
            self.__stock = quantity

    def display_information(self):
        print(f"ID: {self.__product_id}\nName: {self.__name}\nPrice: ${self.__price}\nStock: {self.__stock}")

    def get_product_id(self):
        return self.__product_id

    def get_name(self):
        return self.__name

    def get_price(self):
        return self.__price 

    def get_stock(self):
        return self.__stock
