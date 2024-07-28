from Foodmanager import FoodManager
from Cart import Cart

class MainMenu:

    __Options = {1: "Show Restaurants", 2: "Show FoodItems", 3: "Search Restaurants", 4: "Search FoodItems",
                 5: "LogOut"}

    def __init__(self):
        self.__FoodManager = FoodManager()

    def ShowRestaurants(self):
        for i, res in enumerate(self.__FoodManager.Restaurants, 1):
            res.DisplayItems(i)
        print()

        choice = int(input("Choose the Restaurant: "))
        if 1 <= choice <= len(self.__FoodManager.Restaurants):
            res = self.__FoodManager.Restaurants[choice - 1]
            self.ShowFoodMenus(res.FoodMenu)
        else:
            print("Invalid choice")

    def ShowFoodItems(self, fooditems=None):
        if fooditems is not None:
            for i, foo in enumerate(fooditems, 1):
                foo.DisplayItems(i)

            choices = list(map(int, input("Choose Your Food Items (e.g., 1,2): ").split(',')))
            Cart1 = Cart(fooditems, choices)
            Cart1.ProcessOrder(fooditems)
        else:
            for i, res in enumerate(self.__FoodManager.FoodItems, 1):
                res.DisplayItems(i)
                print()


    def SearchRestaurants(self):
        resName = input("Enter Restaurant Name: ")
        res1 = self.__FoodManager.FindRestaurant(resName)

        if res1 is not None:
            print("Restaurant Found...!")
            print(f"Name: {res1.Name}, Rating: {res1.Ratings}, Offer: {res1.Offer}")
            self.ShowFoodMenus(res1.FoodMenu)
        else:
            print(f"No Restaurant found with the name {resName}")

    def SearchFoodItems(self):
        foodname = input("Enter Food Name: ")
        found = False

        for item in self.__FoodManager.FoodItems:
            if foodname.lower() in item.Name.lower():
                print(f"{item.Name} is Found...!")
                item.DisplayItems(1)
                found = True
        if not found:
            print("No food item found")

    def ShowFoodMenus(self, menus):

        print("\nList of Food Menus Available:- ")
        for i, menu in enumerate(menus, 1):
            menu.DisplayItems(i)
        print()
        choice = int(input("Choose Food Menus: "))
        if 1 <= choice <= len(menus):
            fooditems = menus[choice-1].FoodItem
            self.ShowFoodItems(fooditems)
        else:
            print("Invalid choice")


    def LogOut(self):
        print("You have been Successfully Logged Out..!")
        exit()

    def Start(self):
        while True:

            for i in MainMenu.__Options:
                print(f"{i}. {MainMenu.__Options[i]}", end=" ")
            print()

            try:
                choice = int(input("Enter Any of the Option: "))
                value = (MainMenu.__Options[choice]).replace(" ", "")
                getattr(self, value)()
            except (ValueError, KeyError):
                print("Invalid Input,.. Please Enter Valid Input")
