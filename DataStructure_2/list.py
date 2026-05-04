# A list is an ordered collection of items where elements can be changed, added, or removed.

# Allows duplicates

# Indexed

# Mutable

# create empty list
my_list = []
new_list = list()

# 1. append() — Add item at the end
a = [1, 2, 3]
a.append(4)
print(a)   # [1, 2, 3, 4]

# time complexity of append() is O(1) because it adds an element at the end of the list without needing to shift any existing elements.

# 2. extend() — Add all items of another list
listA = [1, 2, 3]
listB = [4, 5, 6]
listA.extend(listB)
print(listA)   # [1, 2, 3, 4, 5, 6]

# time complexity of extend() is O(k), where k is the number of elements being added from the other list. This is because it needs to iterate through the new list to add each element to the original list.

# 3. insert() — Add item at a specific index
b = [10, 20, 30]
b.insert(1, 99)
print(b)   # [10, 99, 20, 30]

# time complexity of insert() is O(n) in the worst case, where n is the number of elements in the list. This is because inserting an element at a specific index may require shifting all subsequent elements to the right to make space for the new element.

# 4. pop() — Remove and return an item by index
c = [10, 20, 30, 40]
removed_item = c.pop(2)
print(removed_item)   # 30
print(c)              # [10, 20, 40]

# time complexity of pop() is O(n) in the worst case when popping an element from the middle or beginning of the list, as it requires shifting subsequent elements to fill the gap. However, if popping from the end of the list (pop()), it has a time complexity of O(1) since no shifting is needed.

# 5. remove() — Remove first occurrence of a value
d = [1, 2, 3, 2]
d.remove(2)
print(d)   # [1, 3, 2]
# time complexity of remove() is O(n) in the worst case, where n is the number of elements in the list. This is because it needs to search through the list to find the first occurrence of the specified value and then remove it, which may require shifting subsequent elements to fill the gap. 

# 6. clear() — Remove all elements
e = [1, 2, 3]
e.clear()
print(e)   # []

# time complexity of clear() is O(1) because it simply resets the list to an empty state without needing to iterate through the elements.


# 7. sort() — Sort the list (ascending by default) 
f = [4, 2, 1, 3]
f.sort()
print(f)   # [1, 2, 3, 4]

# time complexity of sort() is O(n log n) on average, where n is the number of elements in the list. This is because Python's built-in sort() function uses Timsort, which is a hybrid sorting algorithm derived from merge sort and insertion sort. In the worst case, it can degrade to O(n^2) if the list is already sorted in reverse order, but this is rare in practice.

# Descending order:
f.sort(reverse=True)

#  The reverse parameter simply changes the order of sorting but does not affect the underlying time complexity of the sorting process.

# Custom sorting using key:
names = ["Alice", "Bob", "Charlie"]
names.sort(key=len)  # Sort by length of names
names.sort(key=lambda x: x[0])  # Sort by first character
print(names)  # ['Bob', 'Alice', 'Charlie']

# 8. reverse() — Reverse the list
g = [1, 2, 3]
g.reverse()
print(g)   # [3, 2, 1]

# time complexity of reverse() is O(n) because it needs to iterate through the entire list to reverse the order of the elements. Each element is accessed and swapped, resulting in a linear time complexity relative to the number of elements in the list.

# 9. count() — Count occurrences
h = [1, 2, 2, 3]
print(h.count(2))   # 2
# time complexity of count() is O(n) because it needs to iterate through the entire list to count the occurrences of the specified value. Each element is checked against the target value, resulting in a linear time complexity relative to the number of elements in the list.

# 10. index() — Get index of first occurrence
i = [10, 20, 30]
print(i.index(20))   # 1
# time complexity of index() is O(n) because it needs to iterate through the list to find the first occurrence of the specified value. In the worst case, it may need to check every element in the list, resulting in a linear time complexity relative to the number of elements in the list.

# 11. copy() — Shallow copy of a list
listX = [1, 2, 3]
listY = listX.copy()
print(listY)   # [1, 2, 3]  and memory address will be different of listY


# time complexity of copy() is O(n) because it needs to create a new list and copy each element from the original list to the new list. This involves iterating through all elements in the original list, resulting in a linear time complexity relative to the number of elements in the list.

# 12. len() — Get length
j = [10, 20, 30]
print(len(j))   # 3

# time complexity of len() is O(1) because it returns the number of items in the list, which is stored as an attribute of the list object. This means that it can retrieve the length in constant time without needing to iterate through the elements of the list.

# 13. Using 'in' to check membership
print(3 in [1, 2, 3])   # True

# time complexity of the 'in' operator for lists is O(n) in the worst case, where n is the number of elements in the list. This is because it needs to iterate through the list to check if the specified value exists, and in the worst case, it may need to check every element before finding a match or determining that the value is not present.

# 14. List slicing [start:end] and end is exclusive
k = [10, 20, 30, 40, 50]
print(k[1:4])   # [20, 30, 40]

# time complexity of list slicing is O(k), where k is the number of elements in the slice. This is because it creates a new list containing the sliced elements, which requires iterating through the specified range of elements to copy them into the new list. The time complexity is linear relative to the size of the slice being created.

# 15. max() / min()
m = [5, 10, 2]
print(max(m))  # 10
print(min(m))  # 2

# time complexity of max() and min() is O(n) because they need to iterate through the entire list to find the maximum or minimum value. Each element is compared to determine if it is greater than (for max) or less than (for min) the current maximum or minimum, resulting in a linear time complexity relative to the number of elements in the list.

