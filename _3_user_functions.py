class user:

    def __init__(self,name,phone_number,email,address,password):
        self.name = name
        self.email = email
        self.phone_number = phone_number
        self.address = address
        self.password = password

    def __str__(self):
        return f"Name: {self.name}\nPhone Number: {self.phone_number}\nEmail: {self.email}\nPassword: {self.password}\nAddress: {self.address}"
    
    def get_name(self):
        return self.name
    def set_name(self,name):
        self.name = name
    
    def get_email(self):
        return self.email
    def set_email(self,email):
        self.email = email
    
    def get_phone_number(self):
        return self.phone_number
    def set_phone_number(self,phone_no):
        self.phone_number = phone_no
    
    def get_password(self):
        return self.password
    def set_password(self,password):
        self.password = password
    
    def get_address(self):
        return self.address
    def set_address(self,address):
        self.address = address


class userOperations:
    users_info_list = []

    def register(self):
        name = input("Enter your Full Name: ")
        phone_no = int(input("Enter your phone number: "))
        email_id = input("Enter email id: ")
        address = input("Enter your adress: ")
        password = input("Create new password: ")
        user_obj = user(name=name,phone_number=phone_no,email=email_id,address=address,password=password)
        self.users_info_list.append(user_obj)
        return user_obj
    
    def user_login(self):
        email = input("Enter email: ")
        password = input("Enter password: ")

        for i in self.users_info_list:

            # print("HERE",i.get_email(),i.get_password())

            if i.get_email() == email and i.get_password() == password:
                print("Login Successfull!!!")
                choice = int(input(f"1.Place new order\n2.order history\n3.Update Profile\n Enter choice: "))
            
                if choice == 1:
                    print("*****Place New Order*****")
                    menu_list = {"1":"Tandoori chicken (4 pieces) - INR 240", "2": "Vegan burger (1 piece) - INR 320", "3": "Truffle cake (500gm) - INR 900 "}
                    choice = list((input("Food list: \n1.Tandoori chicken (4 pieces) - INR 240 \n2.Vegan burger (1 piece) - INR 320 \n3.Truffle cake (500gm) - INR 900 \nselect your order")))
                    if choice!=None:
                        self.order_list=[]
                        for i in choice:
                            self.order_list.append(menu_list[i])
                        print("order list")
                            
                        for i in self.order_list:
                            print("*",i)
                        confirmation = int(input("Press 1 to place the order"))

                        if confirmation==1:
                            print("Order Placed Sucessfully")
                            self.order_history.append(self.order_list)      
                        else:
                            print("items moved to wishlist")
                        return self.order_list
                    
                elif choice ==2:
                    print("*****Order history******")                   
                    for i in self.order_history:
                        print(i)

                elif choice ==3:
                    print("*****Update Profile******")
                    name = input("Enter name : ")
                    phone_no = input("Enter New mobile no. : ")
                    email_id = input("Enter New Email id : ")
                    address = input("Enter New Address : ")
                    pswd = int(input("Enter new password: "))
                    i.set_name(name)
                    i.set_phone_number(phone_no)
                    i.set_email(email_id)
                    i.set_address(address)
                    i.set_password(pswd)
                    print("Profile updated Successfully!!!")
                    return self.users_info_list
                else:
                    print("invalid input")



        else:
            print("invalid mail id or password")

        
        

    
# obj = userOperations()
# obj.register()
# obj.user_login()
