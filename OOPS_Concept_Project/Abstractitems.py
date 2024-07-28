from abc import ABC, abstractmethod


class AbstractItems(ABC):

    def __init__(self, name, ratings=None):
        self.Name = name
        self.Ratings = ratings

    @abstractmethod
    def DisplayItems(self, start):
        pass