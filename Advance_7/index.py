# 1️⃣ Lambda Functions
# Small anonymous functions — perfect for one-line logic.
# Use when: You need a tiny function only once.
# same like arrow function in javascript

add = lambda a, b: a + b
print(add(5, 7))

# 2️⃣ map()
# Applies a function to every element in an iterable.
# Use when: Transforming lists without loops.

nums = [1, 2, 3, 4] 

squared = list(map(lambda x: x*x, nums))
print(squared)

def mul (x) :
    return x * 2

twice = list(map(mul,nums))
print(f"The  twice of the  number list is {twice}")

# 3️⃣ filter()
# Keeps elements that return True for a condition.
# Use when: You want only items that satisfy a condition.

nums = [1, 2, 3, 4, 5, 6]
even = list(filter(lambda x: x % 2 == 0, nums)) # why here explicityly mention the list()
print(even)

# 4️⃣ sorted()
# Sort any iterable with custom logic.
# Use when: You want sorting beyond default behavior.

students = [("Dipu", 88), ("Sam", 70), ("Ravi", 92)]
sorted_by_marks = sorted(students, key=lambda x: x[1])
sorted_by_Names = sorted(students, key= lambda x:x[0])

print(sorted_by_Names)
print(sorted_by_marks)

# 5️⃣ List Comprehensions
# Cleaner alternative to loops.
# Use when: You want fast + clean data processing.

nums = [1, 2, 3, 4]
squared = [x*x for x in nums]
print(squared)

# 6️⃣ Dictionary Comprehensions
# Quick creation of dictionaries.

data = ['a', 'b', 'c']
index_map = {i: v for i, v in enumerate(data)} # why here enumerater is used 
print(index_map)

# 7️⃣ Zip
# Combine multiple iterables together.

names = ["a", "b", "c"]
scores = [90, 80, 70]
combined = list(zip(names, scores))
print(f" the zipped form {combined}")

# 8️⃣ Enumerate
# Get index + value while looping.

for i, value in enumerate(["x", "y", "z"]):
    print(i, value)

# 9️⃣ Try / Except / Finally  :(mainly use for the asynchorous task)
# Handle errors gracefully.

try:
    x = 5 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")
finally:
    print("Done")

# 🔟 Context Manager (with)
# Automatically handles open/close, acquire/release.

with open("file.txt", "r") as f:
    data = f.read()



# Custom context manager:

from contextlib import contextmanager

@contextmanager
def my_resource():
    print("Start")
    yield
    print("End")

with my_resource():
    print("Inside")

# 1️⃣1️⃣ Decorators  
# Add features to functions without modifying them.

def logger(fn):
    def wrapper():
        print("Before")
        fn()
        print("After")
    return wrapper

@logger
def say_hi():
    print("Hi")

say_hi()

# 1️⃣2️⃣ Generators

# Efficient iteration — don't store everything in memory.

def countdown(n):
    while n > 0:
        yield n
        n -= 1

for x in countdown(5):
    print(x)

# 1️⃣4️⃣ Typing (Type Hints)
# Makes your code clean & reduces bugs.

def add(a: int, b: int) -> int:
    return a + b

# 1️⃣5️⃣ Dataclasses
# Auto-generate __init__, __repr__, __eq__, etc.

from dataclasses import dataclass

@dataclass
class User:
    name: str
    age: int

u = User("Dipu", 21)
print(u)