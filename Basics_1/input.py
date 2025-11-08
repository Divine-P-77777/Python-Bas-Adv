# input() is a built-in function in Python

a = int(input("Enter number 1: "))

b = int(input("Enter number 2: "))

print("Number a is: ", a)
print("Number b is: ", b) 
print("Sum is ", a + b)

# By default string but we can change into  int and float if possible

c = input("Enter First name: ") 

d = input("Enter Surname: ")

print("First name is: ", c)
print("Surname is: ", d) 
print("Full name is ", c + "  " + d)


# f"" is a formatted string literal in Python, used to embed expressions (like variables, functions, or calculations) directly inside strings. 

# f"" is beneficial because it simplifies string formatting, improves code readability, handles type conversion automatically, and is more efficient than traditional concatenation. 

name = input("Enter your full name: ")
age = (input("Enter your age: "))

# age = int(input("Enter your age: "))
print(f"My name is {name} and I am {age} years old.") #  just like  template  literals 



print("My name is " + name + " and I am " + age + " years old") 
# TypeError: can only concatenate str (not "int") to str
