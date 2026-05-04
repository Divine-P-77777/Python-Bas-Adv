import time


def WhileLoop():
    i = 0
    while i < 1000:
        print(i)
        i += 1


def ForLoop():
    for i in range(1000):
        print(i)


# init = time.time()  # gives in seconds

# # WhileLoop()
# ForLoop()
# print("While Loop Time:", time.time() - init)

# print("\n You are...")
# time.sleep(2)  # Pauses the program for 2 seconds
# print("Awesome!")

t = time.localtime()  # gives in struct_time format
print(t)

formated_time = time.strftime("%Y-%m-%d %H:%M:%S", t)
print(formated_time)