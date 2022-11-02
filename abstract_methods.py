'''public - it is easily accessible by any part of the program
private  - It is only accessible by the class itself. It cant be accessed outside class body
protected - The members of a class that are declared protected are only accessible to a class derived from it


Abstraction -  hiding / restricting the data
inheritance - Parent / child relationship
Encapsulation - Entire class concept
polymorphisam - method overloading and overriding

'''



class parent():

    def __init__(self,name,age):
        self._name = name
        self.__age = age


    def playground(self): # public method
        pass

    def _house_key(self): #_ protected
        pass

    def __creditcard(self): # __ means private in python
        pass

    def _senior_citizen(self):
        if self.__age > 60:
            print("Parent is a senior citizen")
        else:
            print("Parent is not a senior citizen")


class child(parent):
    pass


c = child('parent name',65)
print(c._name)

c._senior_citizen()








