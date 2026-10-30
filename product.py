class Product:
    def __init__(self, _Product__id, _Product__name, _Product__price, _Product__stock):
        self.__id = _Product__id
        self.__name = _Product__name
        self.__price = _Product__price
        self.__stock = _Product__stock

    def update_stock(self, quantity):
        if quantity >= 0: 
            self.__stock = quantity

    def display_information(self):
        print(f"ID: {self.__id}\nName: {self.__name}\nPrice: ${self.__price}\nStock: {self.__stock}")

    def get_product_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    def get_price(self):
        return self.__price 

    def get_stock(self):
        return self.__stock
