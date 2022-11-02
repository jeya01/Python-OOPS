'''
OOP Exercise 1: Create a Class with instance attributes
Write a Python program to create a Vehicle class with max_speed and mileage instance attributes
'''

# class Vehicle:
#     def __init__(self,max_speed,milage):
#         self.max_speed = max_speed
#         self.milage = milage
#
# v = Vehicle(10,20)
# print(v.max_speed,v.milage)


'''OOP Exercise 2: Create a Vehicle class without any variables and methods'''

# class Vehicle:
#     pass


'''OOP Exercise 3: Create a child class Bus that will inherit all of the variables and methods of the Vehicle class'''

# class Vehicle:
#
#     def __init__(self, name, max_speed, mileage):
#         self.name = name
#         self.max_speed = max_speed
#         self.mileage = mileage
#     def vehicle_name(self):
#         print("Vehicle Name:", self.name)
#     def vehicle_speed(self):
#         print("The speed:", self.max_speed)
#     def vehicle_milage(self):
#         print("The milage:",self.mileage)
# class Bus(Vehicle):
#     pass
#
# bus = Bus("Bus" , 30 , 20)
# bus.vehicle_name()
# bus.vehicle_speed()
# bus.vehicle_milage()

'''Create a Bus class that inherits from the Vehicle class. Give the capacity argument of Bus.seating_capacity()
 a default value of 50. '''

# class Vehicle:
#     def __init__(self, name, max_speed, mileage):
#         self.name = name
#         self.max_speed = max_speed
#         self.mileage = mileage
#
#     def seating_capacity(self,capacity):
#         return f"The seating capacity of a {self.name} is {capacity} passengers"
#
# class Bus(Vehicle):
#     def seating_capacity(self,capacity=50):
#         return super().seating_capacity(capacity=50)
#
# bus = Bus("school bus",20,30)
# print(bus.seating_capacity())


'''OOP Exercise 5: Define a property that must have the same value for every class instance (object)
Define a class attribute”color” with a default value white. I.e., Every Vehicle should be white.'''

'''Variables created in .__init__() are called instance variables. 
An instance variable’s value is specific to a particular instance of the class. For example, in the solution, 
All Vehicle objects have a name and a max_speed, but the name and max_speed variables’
 values will vary depending on the Vehicle instance.

On the other hand, the class variable is shared between all class instances. 
You can define a class attribute by assigning a value to a variable name outside of .__init__().'''
class Vehicle:
    color = "white"

    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

class Bus(Vehicle):
    pass


class Car(Vehicle):
    pass

bus = Bus("school bus",20,30)
print(bus.color,bus.name,bus.max_speed,bus.mileage)