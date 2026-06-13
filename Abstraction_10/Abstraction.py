# Abstraction is about reducing complexity. You expose only the necessary details to the user and hide all the complicated internal logic. The user doesn't need to know how things work inside, just that they work.




from abc import ABC, abstractmethod

class Shape (ABC):
    @abstractmethod
    def area(self):
        pass
    @abstractmethod
    def perimeter(self):
        pass

# s = Shape() # can't  create object instance     

#Concrete Class
class Rectangle(Shape):
    def __init__(self, length : int, breadth : int):
        self.length = length
        self.breadth = breadth

    def area(self):
        print(self.length*self.breadth)    
    def perimeter(self):
        print(2 * (self.length + self.breadth))    



rect = Rectangle(3,5)

rect.area()
rect.perimeter()
    