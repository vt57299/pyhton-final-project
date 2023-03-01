from _3_user_functions import user,userOperations

class Main:
    def execute(self,choice):
        if choice == 1:
            print("*****Registeration*****")
            obj2.register()
        
        if choice == 2:
            print("*****Login*****")
            obj2.user_login()

if __name__ == "__main__":
    obj1 = Main()
    obj2 = userOperations()
    while True:
        choice = int(input("1.Register \n2.Login \nEnter : "))
        obj1.execute(choice)