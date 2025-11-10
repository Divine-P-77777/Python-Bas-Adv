# Slicing
name = "DynamicPhillic"

nameshort = name[0:7] # start from index 0 all the way till 7 (excluding 7)
print(nameshort)

character1 = name[1] #it prints the  character at index number 1
print(character1)

# Negative Slicing

name = "Deepak" # here indexing like -6,-5,-4,-3,-2,-1

print(name[0:3])

print(name[-4: -1])
print(name[1:4])

print(name[:4]) # is same as print(name[0:4])
print(name[1:]) # is same as print(name[1:5])
print(name[1:5])

# Sting Function

name = "deepak"

print(len(name))
print(name.endswith("rry"))
print(name.startswith("dee"))
print(name.capitalize())

# escape sequence 
a = 'Deepak is a good boy\nbut not a bad \'boy\''
print(a)


# \t: Horizontal Tab - Inserts a horizontal tab space.
print("Name:\tJohn")


# \\: Backslash - Inserts a literal backslash character. 
print("C:\\Users\\User")


# \': Single Quote - Inserts a single quote character within a single-quoted string.
print('It\'s a beautiful day.')

#append
greeting = "Hello"
greeting += "Deepak"

print(greeting)