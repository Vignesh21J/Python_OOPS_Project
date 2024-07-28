from Registering import User
from Userdata import UserData
from Mainmenu import MainMenu
import re

class EnteringSystem:

    def validate_mobile(self, mobile):
        return len(str(mobile)) == 10 and str(mobile).isdigit()

    def validate_email(self, email):
        return re.match(r"[^@]+@[^@]+\.[^@]+", email) is not None

    def validate_password(self, password):
        return re.match(r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[,.@#$&^]).{8,}$', password) is not None


    def Login(self):
        MailID = input("Email I'D: ")
        PassWord = input("Password: ")

        if not self.validate_email(MailID):
            print("Invalid Email ID")
            return

        if not self.validate_password(PassWord):
            print("Password must be at least 8 characters long")
            return

        LoginUsers = UserData.ValidateLogin(MailID, PassWord)

        if LoginUsers is not None:
            print("You have been Successfully Logged In")
            menu = MainMenu()
            menu.Start()
        else:
            print("InValid MailID/PassWord")

    def Register(self):
        Name = input("Name: ")
        Mobile = int(input("Mobile Number: "))
        MailId = input("Email I'D: ")
        Password = input("Password: ")

        if not self.validate_mobile(Mobile):
            print("Invalid Mobile Number")
            return

        if not self.validate_email(MailId):
            print("Invalid Email ID")
            return

        if not self.validate_password(Password):
            print("Password must be at least 8 characters long")
            return

        user = User(Name, Mobile, MailId, Password)
        UserData.AddUser(user)

    def Guest(self):
        print("Guest mode activated. Please login or register to place an order.")

    def Exit(self):
        print("Thank You, Visit Again")
        exit()

    def ValidateOption(self, choice):
        getattr(self, choice)()


class FoodApp:

    EnteringOptions = {1: "Login", 2: "Register", 3: "Guest", 4: "Exit"}

    @staticmethod
    def FirstStep():
        print("<< Welcome To Online Food Ordering Application...>>")

        Enteringsystem = EnteringSystem()

        while True:

            for i in FoodApp.EnteringOptions:
                print(f"{i}. {FoodApp.EnteringOptions[i]}", end=" ")
            print()

            try:
                choice = int(input("Enter Any of the Option: "))
                Enteringsystem.ValidateOption(FoodApp.EnteringOptions[choice])
            except (ValueError, KeyError):
                print("Invalid Input,.. Please Enter Valid Input")


FoodApp.FirstStep()

