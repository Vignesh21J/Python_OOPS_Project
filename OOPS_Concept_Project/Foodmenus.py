from Abstractitems import AbstractItems
from Fooditems import FoodItems


class FoodMenus(AbstractItems):

    def __init__(self, name):
        super().__init__(name)
        self.__FoodItem = []

    @property
    def FoodItem(self):
        return self.__FoodItem

    @FoodItem.setter
    def FoodItem(self, items):

        for i in items:
            if not isinstance(i, FoodItems):
                print("InValid FoodItems...")
                return

        self.__FoodItem = items

    def DisplayItems(self, start):
        print(f"{start}. {self.Name}")
