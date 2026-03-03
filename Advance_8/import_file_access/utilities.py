def greet(name):
    """Prints a greeting message."""
    return f"Hello, {name}!"

# This code block only runs when utilities.py is executed as the main script
if __name__ == "__main__":
    print("Running utilities.py directly as a script.")
    message = greet("Alice")
    print(message)
else:
    print("utilities.py is being imported into another module.")
