# Dictionary (Key–Value Pairs)

# A dictionary stores data as key–value pairs.

# Keys are unique

# Values can repeat

# Mutable

# Fast lookups using keys

# 1. get() — Safe key access
data = {"Harry": 100, "Shubham": 56}

print(data.get("Harry"))       # 100
print(data.get("Unknown"))     # None
print(data.get("Unknown", 0))  # 0 (default)

# time complexity of get() is O(1) on average because it uses a hash table to store key-value pairs, allowing for constant time complexity for lookups. However, in rare cases of hash collisions, the time complexity can degrade to O(n), where n is the number of keys in the dictionary, but this is uncommon with a good hash function and proper resizing of the hash table.


# 2. keys() — Returns all keys
print(data.keys())   # dict_keys(['Harry', 'Shubham'])

# time complexity of keys() is O(1) because it returns a view object that provides a dynamic view of the dictionary's keys. This operation does not require iterating through the dictionary or creating a new list of keys, resulting in constant time complexity.

# 3. values() — Returns all values
print(data.values())   # dict_values([100, 56])

# time complexity of values() is O(1) because it returns a view object that provides a dynamic view of the dictionary's values. Similar to keys(), this operation does not require iterating through the dictionary or creating a new list of values, resulting in constant time complexity.


# 4. items() — Returns key-value pairs
print(data.items())
# dict_items([('Harry', 100), ('Shubham', 56)])


# 5. update() — Add or overwrite keys
data.update({"Rohan": 99})
data.update({"Harry": 50})  # Overwrites
print(data)

# time complexity of update() is O(k) where k is the number of key-value pairs being added or updated. This is because it needs to iterate through the new key-value pairs to add them to the dictionary, and in the case of overwriting existing keys, it may also need to check for key existence. However, if only a single key-value pair is being added or updated, the time complexity can be considered O(1) on average due to the underlying hash table implementation of dictionaries in Python.


# 6. pop() — Remove key and return value
info = {"A": 1, "B": 2}
value = info.pop("B")
print(value)   # 2
print(info)    # {'A': 1}

# time complexity of pop() is O(1) on average because it uses a hash table to store key-value pairs, allowing for constant time complexity for lookups and removals. However, in rare cases of hash collisions, the time complexity can degrade to O(n), where n is the number of keys in the dictionary, but this is uncommon with a good hash function and proper resizing of the hash table.


# 7. popitem() — Removes last inserted key-value
record = {"X": 10, "Y": 20}
record.popitem()
print(record)   # {'X': 10}


# 8. clear() — Remove all items
record.clear()
print(record)    # {}


# 9. copy() — Shallow copy
copy_dict = data.copy()  # copy_dict is at a different memory location than data
print(copy_dict)


# 10. Accessing values
# ❌ Raises error
# print(data["Unknown"])   # (Removed to avoid crash)

# ✔ Safe version
print(data.get("Unknown"))


# 11. Using 'in' to check key existence  with O(1) TC
sample = {"P": 5}
print("P" in sample)     # True
print("Z" in sample)     # False


# 12. Looping through dictionary
for key, value in sample.items():
    print(key, value)


# 13. Setting default values
sample.setdefault("NewKey", 0)
print(sample)
