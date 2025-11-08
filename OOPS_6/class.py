# A class is a blueprint for creating objects. It defines attributes (data) and methods (functions) that describe the behavior and properties of the objects.

# An object (or instance) is a specific realization of a class. It has: Instance Attributes: Unique to the object (e.g., harry.language = "JavaScript"). Class Attributes: Shared among all objects (e.g., language = "Python").

# Why are Classes/Objects Better Than Functions?
# Reusability: Classes encapsulate data and methods, making the code reusable and modular.
# Organization: Classes group related properties and behaviors together.
# Inheritance: They allow new classes to inherit properties/methods from existing ones.
# Real-world Modeling: Classes and objects mimic real-world entities better than standalone functions.

class Employee: 
    language = "Py"  # Class attribute
    salary = 1200000  # Class attribute


harry = Employee()  # Object instantiation
harry.name = "Harry"  # Instance attribute for 'harry'
print(harry.name, harry.language, harry.salary)  
# Output: Harry Py 1200000

rohan = Employee()  # Another object instantiation
rohan.name = "Rohan Roro Robinson"  # Instance attribute for 'rohan'
print(rohan.name, rohan.salary, rohan.language)
# Output: Rohan Roro Robinson 1200000 Py




# Instance VS Class
class Employee: 
    language = "Python"  # This is a class attribute
    salary = 1200000     # Another class attribute


# Creating an instance of Employee
harry = Employee()
harry.language = "JavaScript"  # This is an instance attribute
print(harry.language, harry.salary)  # Instance attribute overrides the class attribute for 'language'

 