from Fooditems import FoodItems
from Foodmenus import FoodMenus
from Restaurants import Restaurants


class FoodManager:

    def __init__(self):
        self.Restaurants = self.__PrepareFoodRestaurants()
        self.FoodMenus = self.__PrepareFoodMenus()
        self.FoodItems = self.__PrepareFoodItems()

    def __PrepareFoodItems(self):
        item1 = FoodItems("Veg Biryani", 4.2, 120, "Delicious Veg Biryani")
        item2 = FoodItems("Mushroom Biryani", 4.4, 150, "Yummy Mushroom Biryani")
        item3 = FoodItems("Veg Noodles", 4.3, 100, "Spicy Veg Noodles")
        item4 = FoodItems("Chicken Biryani", 4.5, 200, "Tasty Chicken Biryani")
        item5 = FoodItems("Chicken Noodles", 4.6, 120, "Crispy Chicken Noodles")
        item6 = FoodItems("Schezwan Noodles", 4.7, 150, "Schezwan Noodles")
        item7 = FoodItems("Parotta", 4.1, 20, "Parotta with Tasty Sidedish")
        item8 = FoodItems("Dosa", 4.1, 40, "Dosa with Tasty Chutney")

        return [item1, item2, item3, item4, item5, item6, item7, item8]

    def __PrepareFoodMenus(self):
        Fooditem_storing = self.__PrepareFoodItems()

        menu1 = FoodMenus("Veg")
        menu1.FoodItem = [Fooditem_storing[0], Fooditem_storing[1], Fooditem_storing[2], Fooditem_storing[7]]
        menu2 = FoodMenus("Non-Veg")
        menu2.FoodItem = [Fooditem_storing[3], Fooditem_storing[4], Fooditem_storing[5], Fooditem_storing[6]]
        menu3 = FoodMenus("Chinese")
        menu3.FoodItem = [Fooditem_storing[5]]
        return [menu1, menu2, menu3]

    def __PrepareFoodRestaurants(self):
        Foodmenu_storing = self.__PrepareFoodMenus()

        res1 = Restaurants("JKans", 4.6, "Periyar, Madurai", "10%")
        res1.FoodMenu = [Foodmenu_storing[1], Foodmenu_storing[2]]
        res2 = Restaurants("K Subbu", 4.5, "Anna Nagar, Mdu", "15%")
        res2.FoodMenu = [Foodmenu_storing[0], Foodmenu_storing[1]]
        res3 = Restaurants("Sree Sabarees", 4.3, "Villapuram, Mdu", "5%")
        res3.FoodMenu = [Foodmenu_storing[0]]
        res4 = Restaurants("Pechiamman", 4.2, "Villapuram, Mdu", "5%")
        res4.FoodMenu = [Foodmenu_storing[1]]
        return [res1, res2, res3, res4]

    def FindRestaurant(self, name):
        for i in self.Restaurants:
            if i.Name.lower() == name.lower():
                return i
        return None

