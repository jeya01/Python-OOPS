from abc import ABC, abstractmethod




class Vehicle(ABC):

    @abstractmethod
    def tyre(self):
        pass
    @abstractmethod
    def rear_view_mirror(self):
        pass

class Maruthi(Vehicle):
    def tyre(self):
        print("this is maruthi tyre")
    def rear_view_mirror(self):
        print("this is maruthi mirror")



# https://pynative.com/python-object-oriented-programming-oop-exercise/
