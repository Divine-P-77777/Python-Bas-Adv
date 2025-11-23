# A list is an ordered collection of items where elements can be changed, added, or removed.

# Allows duplicates

# Indexed

# Mutable


# 1. append() — Add item at the end
a = [1, 2, 3]
a.append(4)
print(a)   # [1, 2, 3, 4]


# 2. extend() — Add all items of another list
listA = [1, 2, 3]
listB = [4, 5, 6]
listA.extend(listB)
print(listA)   # [1, 2, 3, 4, 5, 6]


# 3. insert() — Add item at a specific index
b = [10, 20, 30]
b.insert(1, 99)
print(b)   # [10, 99, 20, 30]


# 4. pop() — Remove and return an item by index
c = [10, 20, 30, 40]
removed_item = c.pop(2)
print(removed_item)   # 30
print(c)              # [10, 20, 40]


# 5. remove() — Remove first occurrence of a value
d = [1, 2, 3, 2]
d.remove(2)
print(d)   # [1, 3, 2]


# 6. clear() — Remove all elements
e = [1, 2, 3]
e.clear()
print(e)   # []


# 7. sort() — Sort the list (ascending by default)
f = [4, 2, 1, 3]
f.sort()
print(f)   # [1, 2, 3, 4]

# Descending order:
f.sort(reverse=True)


# 8. reverse() — Reverse the list
g = [1, 2, 3]
g.reverse()
print(g)   # [3, 2, 1]


# 9. count() — Count occurrences
h = [1, 2, 2, 3]
print(h.count(2))   # 2


# 10. index() — Get index of first occurrence
i = [10, 20, 30]
print(i.index(20))   # 1


# 11. copy() — Shallow copy of a list
listX = [1, 2, 3]
listY = listX.copy()
print(listY)   # [1, 2, 3]


# 12. len() — Get length
j = [10, 20, 30]
print(len(j))   # 3


# 13. Using 'in' to check membership
print(3 in [1, 2, 3])   # True


# 14. List slicing
k = [10, 20, 30, 40, 50]
print(k[1:4])   # [20, 30, 40]


# 15. max() / min()
m = [5, 10, 2]
print(max(m))  # 10
print(min(m))  # 2
