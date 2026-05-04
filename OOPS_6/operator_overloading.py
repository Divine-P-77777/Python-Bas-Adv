class Number:
    def __init__(self, n):
        self.n = n

    def __add__(self, num):  # # 👈 Overloading the + operator
        return self.n + num.n  # # adds two Number objects

n = Number(1)
m = Number(2)

print(n + m)

# n + m
#  ↓
# n.__add__(m)
#  ↓
# self = n (1), num = m (2)
#  ↓
# return 1 + 2
#  ↓
# 3

# Python lets you do this by defining special methods like:

# __add__ → for +

# __sub__ → for -

# __mul__ → for *

# __eq__ → for ==
# …and so on.






# 💥 What happens behind the scenes:

# n + m   →   n.__add__(m)


# That calls:

# return self.n + num.n

class Number:
    def __init__(self, n):
        self.n = n

    def __add__(self, num):
        return self.n + num.n
    def __mul__(self, num):
        return self.n * num.n
# So output = 4 + 2 = 6

# Operator overloading = teaching Python how to use operators (+, -, etc.) with your own classes.