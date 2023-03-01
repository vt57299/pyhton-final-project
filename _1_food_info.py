class Food:
    def __init__(self,food_ID,food_name,food_quantity,food_price,food_discount,food_stock):
        self.food_ID = food_ID
        self.food_name = food_name
        self.food_quantity = food_quantity
        self.food_price = food_price
        self.food_discount = food_discount
        self.food_stock = food_stock

    def __str__(self):
        return f"food ID: {self.food_ID}\nFood Name: {self.food_name}\nQuantity: {self.food_quantity}\nPrice: {self.food_price}\nDiscount: {self.food_discount}\nStock: {self.food_stock}"


    # Encapsulation
    def get_food_ID(self):
        return self.food_ID
    def set_food_ID(self,food_ID):
        self.food_ID = food_ID

    def get_food_name(self):
        return self.food_name
    def set_food_name(self,food_name):
        self.food_name = food_name

    def get_food_quantity(self):
        return self.food_quantity
    def set_food_quantity(self,quantity):
        self.food_quantity = quantity

    def get_food_price(self):
        return self.food_price
    def set_food_price(self,price):
        self.food_price = price

    def get_food_discount(self):
        return self.food_discount
    def set_food_discount(self,discount):
        self.food_discount = discount

    def get_food_stock(self):
        return self.food_stock
    def set_food_stock(self,stock):
        self.food_stock = stock