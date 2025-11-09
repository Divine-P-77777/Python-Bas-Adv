# Self

# self is used in instance methods
# self is required for normal functions (methods) inside a class that work on a particular object.
# It refers to the current instance of the class.

class Employee: 
    language = "Python" # This is a class attribute
    salary = 1200000

    def getInfo(self):
        print(f"The language is {self.language}. The salary is {self.salary}")

    @staticmethod #It does not use self or cls — it’s just a regular function inside a class that’s grouped there for organization.
    def greet():
        print("Good morning")


dynamic = Employee()
# dynamic.language = "JavaScript" # This is an instance attribute
dynamic.greet()
dynamic.getInfo() 
# Employee.getInfo(dynamic)
 



# Constuctor
# A constructor is a special function in a class that runs automatically when you create an object.
# It is used to set up (initialize) the object with some data.

class Employee: 
    language = "Python" # This is a class attribute
    salary = 1200000

    def __init__(self, name, salary, language): # dunder method which is automatically called
        self.name = name
        self.salary = salary
        self.language = language
        print("I am creating an object")
 
 
    def getInfo(self):
        print(f"The language is {self.language}. The salary is {self.salary}")

    @staticmethod
    def greet():
        print("Good morning")


dynamic = Employee("dynamic", 1300000, "JavaScript") 
# dynamic.name = "dynamic"
print(dynamic.name, dynamic.salary, dynamic.language)

rohan = Employee()


# Behind  the scene  
# 💡 Step-by-step:

# When you write:

# e = Employee("Dipu", 50000, "Python")


# Python automatically calls:

# e.__init__("Dipu", 50000, "Python")


# Inside __init__, it saves those values in the object:

# self.name = "Dipu"
# self.salary = 50000
# self.language = "Python"


# Now your object e has its own data:

# e.name → "Dipu"
# e.salary → 50000
# e.language → "Python"

#  In short:

# Constructor = automatic setup function
# that runs when you create an object
# and fills it with initial values.