
# The Walrus Operator is a new addition to Python 3.8 and allows you to assign a value to a variable within an expression. This can be useful when you need to use a value multiple times in a loop, but don't want to repeat the calculation.
# The Walrus Operator is represented by the syntax and can be used in a variety of contexts including while loops and if statements.
# Here's an example of how you can use the Walrus Operator in a while loop:

a = True
print(a:=False)  # Output: False


numbers = [1, 2, 3, 4, 5]


# without the walrus operator, you would need to write:
foods = list()

# while True:
#     food = input("What food do you like?: ")
#     if food == "quit":
#         break
#     foods.append(food)

# print(foods)



# Keep asking input until user types "quit" using the walrus operator
while (food := input("What food do you like?: ")) != "quit":
    foods.append(food)

# Print result
print(foods)