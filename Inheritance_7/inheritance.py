# Inheritance (1st pillar of oops)
# Inheritance allows one class to acquire the properties and methods of another class. This avoids writing the same code again and again, and makes your codebase much cleaner.
# Parent class (also called base class) contains common, shared features
# Child class (also called derived class) inherits everything from the parent
# Child class can also add its own new attributes and methods on top
# Changes made in the parent class automatically reflect in child classes
# Real life example: Animal class has eat() and sleep(). Dog and Cat inherit these, and Dog adds bark(), Cat adds meow()

class Employee:
    company = "ITC"
    def show(self):
        print(f"The name of the Employee is {self.name} and the salary is {self.salary}")


# class Programmer:
#     company = "ITC Infotech"
#     def show(self):
#         print(f"The name is {self.name} and the salary is {self.salary}")

#     def showLanguage(self):
#         print(f"The name is {self.name} and he is good with {self.language} language")


class Programmer(Employee):
    company = "ITC Infotech"
    def showLanguage(self):
        print(f"The name is {self.name} and he is good with {self.language} language")


a = Employee()
b = Programmer()

print(a.company, b.company)