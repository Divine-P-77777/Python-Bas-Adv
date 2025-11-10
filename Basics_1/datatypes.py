# Python has NO primitive data types.
# All data types are objects, and variables store references to objects.
# Means for each varaible or a function a new object is created in the memory and the variable or function points to that memory location.

a = "31.2"
b = float(a) # a but the type should be float
t = type(b) # type casting

print(t)


c = 4
d = str(c)
e = type(d)

print(e)

f = "1000"
g = int(f)
h = type(g)

print(h)

# Mainly five  Data Types
a = 1 # a is an integer

b = 5.22 # b is a floating point number

c = "Harry" # c is a string

d = False # d is a boolean variable

e = None # e is a none type variable



# Declare Variable with Type (Type Hinting)

age: int = 18
username: str = "admin"
height: float = 5.9
is_logged_in: bool = False

# Numeric Types:
# int: Integers (whole numbers).
# float: Floating-point numbers (numbers with decimal points).
# complex: Complex numbers (numbers with real and imaginary parts).

# Sequence Types:
# str: Strings (sequences of characters).
# list: Ordered, mutable sequences of items.
# tuple: Ordered, immutable sequences of items.
# range: Immutable sequences of numbers, often used for looping.

# Mapping Type:
# dict: Dictionaries (unordered collections of key-value pairs).

# Set Types:
# set: Unordered collections of unique items.
# frozenset: Immutable versions of sets.

# Boolean Type:
# bool: Boolean values (True or False).

# Binary Types:
# bytes: Immutable sequences of bytes.
# bytearray: Mutable sequences of bytes.
# memoryview: A "view" into another object's memory.

# None Type:
# NoneType: Represents the absence of a value, with a single value None.



