from _1_food_info import Food
import random


class adminOperations:
        
    food_list = []

    def addfood(self):
        
        name = input("Enter food name: ")
        quantity = input("Enter quantity(Kg or litre or pcs): ")
        price = float(input("Enter price: "))
        discount = float(input("Enter discount: "))
        stock = input("Enter stock: ")
        ID = random.randint(1,1000)

        food_obj =Food(food_ID = ID,food_name= name,food_quantity=quantity,food_price=price,food_discount=discount,food_stock=stock)
        
        self.food_list.append(food_obj)
        print("Food item added successfully!!!")
        return food_obj

    def viewfooditems(self):
        if len(self.food_list) >0:
            for i in self.food_list:
                print(i,"\n")
        else:
            print("No food items added yet!!!")

    def deletefood(self):
        # Taking the ID of the food item to delete
        food_id = int(input("Enter the ID of the food item to delete: "))


        for food_item in self.food_list:
            if food_item.get_food_ID() == food_id:
                self.food_list.remove(food_item)
                print(f"Food item with food ID {food_id} deleted successfully!!!")
                return self.food_list
            
        else:
            print("You have enter invalid Food ID!!!")


    def editfood(self):
        id = int(input("Enter food id to edit : "))
        for food in self.food_list:
            if food.get_food_ID() == id:
                New_name = input("Enter new food name : ")
                New_quandity = input("Enter new food quantity : ")
                New_price = input("Enter the New food price : ")
                New_discount = input("Enter the New discount : ")
                New_stock = input("Enter New stock : ")
                food.set_food_name(New_name)
                food.set_food_quantity(New_quandity)
                food.set_food_price(New_price)
                food.set_food_discount(New_discount)
                food.set_food_stock(New_stock)
                print("Food item got updated successfully!!!")
                return self.food_list
        else:
            print("Food ID not Found!!!")
        # *********------------------------------******** #

class admin_Main:

    def execute(self,choice):
        if choice == 1:
            print("*****Add Food*****")
            operation.addfood()
        
        elif choice == 2:
            print("*****View Food Items*****")
            operation.viewfooditems()
        elif choice == 3:
            print("*****Edit Food using food ID*****")
            operation.editfood()
        elif choice == 4:
            print("*****Delete food item using food ID*****")
            operation.deletefood()
        

if __name__ == "__main__":
    operation = adminOperations()
    admin_obj = admin_Main()
    while True:
        
        admin_obj.execute(int(input("1.Add Food\n2.View Food items\n3.Edit food Item\n4.REmove food item\nEnter choice:")))