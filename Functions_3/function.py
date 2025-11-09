# a = int(input("Enter your number: "))
# b = int(input("Enter your number: "))
# c = int(input("Enter your number: "))
 
# average = (a + b + c)/3
# print(average)

# a = int(input("Enter your number: "))
# b = int(input("Enter your number: "))
# c = int(input("Enter your number: "))
 
# average = (a + b + c)/3
# print(average)

# Function Definition
def avg():
    a = int(input("Enter your number: "))
    b = int(input("Enter your number: "))
    c = int(input("Enter your number: "))
    
    average = (a + b + c)/3
    print(average)


avg() # Function Call
print("Thank you!")
# avg()
# print("Thank you!")
# avg()
# print("Thank you!")
# avg()
# avg()

def goodDay():
    print("Good Day")

goodDay()




# A lambda function to add two numbers
add = lambda a, b: a + b
print(add(5, 3)) # Output: 8

# A lambda function to double a number
double = lambda x: x * 2
print(double(7)) # Output: 14


# Lambda functions are frequently used as arguments to higher-order functions (functions that take other functions as arguments), such as:


numbers = [1, 2, 3, 4]
squared_numbers = list(map(lambda x: x**2, numbers))
print(squared_numbers) # Output: [1, 4, 9, 16]