# Import the greet function from the utilities module
from utilities import greet

print("Running main_app.py.")

# The code inside the if __name__ == "__main__": in utilities.py is NOT executed here.

def main():
    user_name = "Bob"
    message = greet(user_name)
    print(f"Result in main_app.py: {message}")

if __name__ == "__main__":
    main()
