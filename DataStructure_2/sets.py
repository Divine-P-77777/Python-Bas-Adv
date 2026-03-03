# 3. Set (Unordered, Unique Elements)

# A set is an unordered collection of unique items.
# No duplicates
# Unindexed

# Mutable (elements can be added/removed)
# Items must be immutable

e = set() # Dont use s = {} as it will create an empty dictionary
a = {1, 5, 32, 54, 5, 5, 5}


print(a)

# Set Methods

b = {1, 5, 32, 54, 5, 5, 5, "Harry"}

print(b, type(b))

b.add(566)
print(b, type(b))

# time complexity of add() is O(1) on average because it uses a hash table to store elements, allowing for constant time complexity for insertions. However, in rare cases of hash collisions, the time complexity can degrade to O(n), where n is the number of elements in the set, but this is uncommon with a good hash function and proper resizing of the hash table.

b.remove(1)
print(b, type(b))

# time complexity of remove() is O(1) on average because it uses a hash table to store elements, allowing for constant time complexity for removals. However, in rare cases of hash collisions, the time complexity can degrade to O(n), where n is the number of elements in the set, but this is uncommon with a good hash function and proper resizing of the hash table.


# Union And Intersection

set1 = {1, 45, 6, 78}
set2 = {7, 8, 1, 78}

print(set1.union(set2))
print(set1.intersection(set2))
# time complexity of union() and intersection() is O(n + m) where n and m are the number of elements in the two sets being combined or compared. This is because both operations need to iterate through all elements of both sets to create the resulting set, leading to linear time complexity relative to the total number of elements involved in the operation.

# 1. discard()
c = {1, 2, 3}
c.discard(5)  # No error  ,  it  not found  index
print(c)
# time complexity of discard() is O(1) on average because it uses a hash table to store elements, allowing for constant time complexity for removals. However, in rare cases of hash collisions, the time complexity can degrade to O(n), where n is the number of elements in the set, but this is uncommon with a good hash function and proper resizing of the hash table.


# 2. pop()
d = {10, 20, 30}
x = d.pop() # may give key error 
print(x)
print(d)



#  3. clear()
d.clear()
print(d)   # set()
# time complexity of clear() is O(1) because it simply resets the set to an empty state without needing to iterate through the elements.

# 4. difference()
set3 = {1, 2, 3}
set4 = {2, 3}
print(set3.difference(set4))  # {1}



#  5. symmetric_difference()
set5 = {1, 2, 3}
set6 = {3, 4}
print(set5.symmetric_difference(set6))   # {1, 2, 4}


#  6. update()
u1 = {1, 2}
u2 = {3, 4}
u1.update(u2)
print(u1)   # {1, 2, 3, 4}

# 7. issubset() / issuperset()
print({1, 2}.issubset({1, 2, 3}))   # True
print({1, 2, 3}.issuperset({1, 2})) # True


# 8. isdisjoint()
print({1, 2}.isdisjoint({3, 4}))  # True


# 9. Length
print(len(u1))


# 10. Membership test
print(5 in u1)



# Create a set from a string
my_set = set("abcd")
print(f"Set: {my_set}") 

# Convert the set to a list
my_list = list(my_set)
print(f"List: {my_list}")
