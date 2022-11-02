class Student:
    # class variables
    school_name = 'ABC School'

    # constructor
    def __init__(self, name, age):
        # instance variables
        self.name = name
        self.age = age

    # instance variables
    def show(self):
        print(self.name, self.age, Student.school_name)



    @classmethod
    def change_School(cls, name):
        # access class variable
        print('Previous School name:', cls.school_name)
        cls.school_name = name # the state of the class variable is changed
        print('School name changed to', Student.school_name)

    @staticmethod
    def find_notes(subject_name):
        return ['chapter 1', 'chapter 2', 'chapter 3']


# create object
jessa = Student('Jessa', 12)
# call instance method
jessa.show()

# call class method using the class
Student.change_School('XYZ School')
# call class method using the object
jessa.change_School('PQR School')

# call static method using the class
Student.find_notes('Math')
# call class method using the object
jessa.find_notes('Math')