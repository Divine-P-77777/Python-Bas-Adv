# Destructuring (also called unpacking) is the process of breaking a collection — such as a tuple, list, or other iterable — into individual variables in a single assignment.

#  Basic Syntax:
# a, b = (value1, value2)


# This means:

# a gets value1

# b gets value2


#Example 1: A tuple with two values
point = (10, 20)

# Unpack the tuple into two variables
x, y = point

print(x)  # 10
print(y)  # 20



# Example 2: Swapping Variables (no temp variable!)
#  Destructuring allows clean swapping without a temporary variable.
a = 5
b = 10

# Swap values using tuple unpacking
a, b = b, a

print(a)  # 10
print(b)  # 5


# Example 3: Iterating with Tuple Unpacking

pairs = [(1, 'one'), (2, 'two'), (3, 'three')]

for num, word in pairs:
    print(num, "→", word)  #Each (num, word) tuple is unpacked inside the loop.



# Example 4: Unpacking in a Function Return

def get_coordinates():
    return (5, 8)

x, y = get_coordinates()
print(x, y)  # 5 8


# Partial / Extended Unpacking

# Use * to capture “the rest” of the elements:

values = [1, 2, 3, 4, 5]

a, *b, c = values
print(a)  # 1
print(b)  # [2, 3, 4]
print(c)  # 5


#  The *b collects the middle items as a list.


#  Nested Destructuring
# You can destructure nested tuples or lists directly:

person = ("Gaurav", (21, "India"))

name, (age, country) = person
print(name)     # Gaurav
print(age)      # 21
print(country)  # India
#  Works great with nested data structures.


# Ignoring Values with _
# If you don’t need some values, assign them to _:
a, _, b = (10, 20, 30)
print(a, b)  # 10 30
#  _ is a throwaway variable (common convention).



# Dictionary Destructuring (via keys or .items())
person = {"name": "Alice", "age": 25}

# Destructure values manually
name, age = person.values()
print(name, age)  # Alice 25

# Or unpack key-value pairs
for key, value in person.items():
    print(key, ":", value)



