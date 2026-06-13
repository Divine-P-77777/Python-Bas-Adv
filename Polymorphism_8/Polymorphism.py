# Polymorphism ( 2nd pillar of the oops )
# Poly means many, morph means forms. Polymorphism allows the same method name to behave differently depending on which object calls it. This makes your code highly flexible and extensible.
# Same method name works differently for different classes
# You don't need to remember multiple method names for similar actions
# Method Overriding: Child class provides its own version of a parent's method
# Real life example: A "draw()" method on a Circle draws a circle, on a Rectangle it draws a rectangle different behavior same name,



class Animal:
    def move(self):
        print("I am moving")


class Dog(Animal):
    def move(self):
        print("I am running on 4 legs")


class Bird(Animal):
    def move(self):
        print("I am flying")


# Polymorphism
animals = [Dog(), Bird()]

for animal in animals:
    animal.move()