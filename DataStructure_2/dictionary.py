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


# 2. keys() — Returns all keys
print(data.keys())   # dict_keys(['Harry', 'Shubham'])


# 3. values() — Returns all values
print(data.values())   # dict_values([100, 56])


# 4. items() — Returns key-value pairs
print(data.items())
# dict_items([('Harry', 100), ('Shubham', 56)])


# 5. update() — Add or overwrite keys
data.update({"Rohan": 99})
data.update({"Harry": 50})  # Overwrites
print(data)


# 6. pop() — Remove key and return value
info = {"A": 1, "B": 2}
value = info.pop("B")
print(value)   # 2
print(info)    # {'A': 1}


# 7. popitem() — Removes last inserted key-value
record = {"X": 10, "Y": 20}
record.popitem()
print(record)   # {'X': 10}


# 8. clear() — Remove all items
record.clear()
print(record)    # {}


# 9. copy() — Shallow copy
copy_dict = data.copy()


# 10. Accessing values
# ❌ Raises error
# print(data["Unknown"])   # (Removed to avoid crash)

# ✔ Safe version
print(data.get("Unknown"))


# 11. Using 'in' to check key existence
sample = {"P": 5}
print("P" in sample)     # True
print("Z" in sample)     # False


# 12. Looping through dictionary
for key, value in sample.items():
    print(key, value)


# 13. Setting default values
sample.setdefault("NewKey", 0)
print(sample)
