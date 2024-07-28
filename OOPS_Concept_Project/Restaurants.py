from Abstractitems import AbstractItems
from Foodmenus import FoodMenus


class Restaurants(AbstractItems):

    def __init__(self, name, ratings, location, offer):
        super().__init__(name, ratings)
        self.Location = location
        self.Offer = offer
        self.__FoodMenu = []

    @property
    def FoodMenu(self):
        return self.__FoodMenu

    @FoodMenu.setter
    def FoodMenu(self, items):

        for i in items:
            if not isinstance(i, FoodMenus):
                print("InValid FoodMenus...")
                return

        self.__FoodMenu = items

    def DisplayItems(self, start):
        print(f"{start}. Name= {self.Name}, Ratings= {self.Ratings}")
