'''
a = "a very long string with emails"

emails = []
3 seconds
'''

f = open("file.txt", "r")
data = f.read()
print(data)
f.close()

# File Write

st = "Hey Harry you are amazing"

f = open("myfile.txt", "w")

f.write(st)

f.close()

# File Functions
f = open("file.txt")

# lines = f.readlines()
# print(lines, type(lines))

# line1 = f.readline()
# print(line1, type(line1))

# line2 = f.readline()
# print(line2, type(line2))

# line3 = f.readline()
# print(line3, type(line3))

# line4 = f.readline()
# print(line4, type(line4))

# line5 = f.readline()
# print(line5 =="")
line = f.readline()
while(line != ""):
    print(line)
    line = f.readline()

f.close()