# Tuple (Ordered, Immutable)

# A tuple is an ordered collection of items, but cannot be modified after creation.

# Allows duplicates

# Indexed

# Immutable

# Creating a tuple
t1 = (1, 45, 342, 3424, False, "Rohan", "Shivam")

print(t1)
print(type(t1))

# Tuples are immutable → this will not work:
# t1[0] = 99   # ❌ Error: 'tuple' object does not support item assignment


# Duplicate values allowed
t2 = (1, 45, 342, 3424, False, 45, "Rohan", "Shivam")
print(t2)

# count() — Count occurrences of a value
cnt = t2.count(45)
print(cnt)

# index() — Get first index of a value
idx = t2.index(3424)
print(idx)

# Length of tuple
print(len(t2))




# ⭐ 1. Tuple slicing
t = (10, 20, 30, 40, 50)
print(t[1:4])   # (20, 30, 40)

# ⭐ 2. Tuple concatenation
t3 = (1, 2)
t4 = (3, 4)
t5 = t3 + t4
print(t5)   # (1, 2, 3, 4)

# ⭐ 3. Tuple repetition
t = (5, 10)
print(t * 3)   # (5, 10, 5, 10, 5, 10)

# ⭐ 4. Check membership
t = (1, 2, 3)
print(2 in t)     # True
print(5 in t)     # False

# ⭐ 5. Tuples can be nested
nested = (1, 2, (3, 4), (5, (6, 7)))
print(nested)

# ⭐ 6. Tuples can store mixed types
t = (1, "Harry", True, 3.14)
print(t)

# ⭐ 7. Tuple unpacking

# Extract values directly into variables.

p = (10, 20, 30)
x, y, z = p
print(x, y, z)  # 10 20 30

# ⭐ 8. Single-element tuple

# Very important!

t = (5)      # ❌ Not a tuple, just an integer
t = (5,)     # ✔ Tuple

# ⭐ 9. Using tuple as a dictionary key (allowed, because immutable)
d = { (1, 2): "point" }
print(d[(1, 2)])