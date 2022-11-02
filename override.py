'''Overriding - method defeniation used in different class'''

class Override:
    def __init__(self):
        print("I am a constructor")

    def math(self):
        print("I am insde math in override class")





class Child(Override):
    def __init__(self):
        print("I am child's constructor")

    def math(self):
        print("I am insde math in Child class")


c = Child()
c.math()

'''Static method vs class method decorator
class method cls we can access class variable and method
static method we can access variables or methods
'''