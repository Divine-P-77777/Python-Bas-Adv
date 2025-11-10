# ===============================
# Arithmetic Operators
# ===============================

a = 7
b = 4

print("Addition:", a + b)        # +
print("Subtraction:", a - b)     # -
print("Multiplication:", a * b)  # *
print("Division:", a / b)        # /
print("Floor Division:", a // b) # //
print("Modulus (remainder):", a % b)  # %
print("Exponent:", a ** b)       # **


# ===============================
# Assignment Operators
# ===============================

x = 10
print("\nInitial x:", x)

# x += 5   # x = x + 5
# print("x += 5 →", x)

# x -= 3   # x = x - 3
# print("x -= 3 →", x)

# x *= 2   # x = x * 2
# print("x *= 2 →", x)

# x /= 4   # x = x / 4
# print("x /= 4 →", x)

# x //= 2  # x = x // 2
# print("x //= 2 →", x)

# x %= 3   # x = x % 3
# print("x %= 3 →", x)

# x **= 2  # x = x ** 2
# print("x **= 2 →", x)


# ===============================
# Comparison Operators
# ===============================

p = 5
q = 3

print("\nEqual:", p == q)        # ==
print("Not Equal:", p != q)      # !=
print("Greater Than:", p > q)    # >
print("Less Than:", p < q)       # <
print("Greater or Equal:", p >= q) # >=
print("Less or Equal:", p <= q)    # <=

print("Divisible:", p % q == 0)        # divisible check
print("Not Divisible:", p % q != 0)    # not divisible check


# ===============================
# Logical Operators
# ===============================

print("\nLogical OR")
print("True or False:", True or False)
print("True or True:", True or True)
print("False or True:", False or True)
print("False or False:", False or False)

print("\nLogical AND")
print("True and False:", True and False)
print("True and True:", True and True)
print("False and True:", False and True)
print("False and False:", False and False)

print("\nLogical NOT")
print("not True:", not True)
print("not False:", not False)


# ===============================
# Bitwise Operators (Important)
# ===============================

m = 5   # 101
n = 3   # 011

print("\nBitwise AND:", m & n)   # &
print("Bitwise OR:", m | n)      # |
print("Bitwise XOR:", m ^ n)     # ^
print("Bitwise NOT:", ~m)        # ~
print("Left Shift:", m << 1)     # <<
print("Right Shift:", m >> 1)    # >>


# ===============================
# Membership Operators
# ===============================

nums = [1, 2, 3, 4]

print("\nMembership Operators")
print("2 in nums:", 2 in nums)
print("5 not in nums:", 5 not in nums)


# ===============================
# Identity Operators
# ===============================

a = 10
b = 10
c = [1, 2, 3]   # creates a list at memory location A
d = [1, 2, 3]   # creates another list at memory location B

print("\nIdentity Operators")
print("a is b:", a is b)
print("c is d:", c is d)
print("c == d:", c == d)
