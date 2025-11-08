a = (1,45,342,3424,False, "Rohan", "Shivam")
# a [0] = False  # it doesnt work because  'tuple' object does not support item assignment they are immutable
print(a)
print(type(a))


a = (1,45,342,3424,False, 45, "Rohan", "Shivam")
print(a) 

no = a.count(45)
print(no)

i = a.index(3424)
print(i)

print(len(a))