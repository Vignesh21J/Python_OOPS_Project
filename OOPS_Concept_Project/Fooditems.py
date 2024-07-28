from Abstractitems import AbstractItems


class FoodItems(AbstractItems):

    def __init__(self, name, rating, price, description):
        super().__init__(name, rating)
        self.Price = price
        self.Description = description

    def DisplayItems(self, start):
        print(f"{start}. Name: {self.Name}, Price: {self.Price}, Description: {self.Description}")
