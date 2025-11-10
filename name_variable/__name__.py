# __name__ is a built-in variable in every Python file.

# When a file is run directly, Python sets:

__name__ = "__main__"


# When a file is imported, Python sets:

__name__ = "<module_name>"

# ✅ Purpose

# Controls when code should execute

# Prevents unwanted execution during imports

# Separates reusable logic from script execution

# 🧠 Syntax
if __name__ == "__main__":
    # code runs only when file is executed directly

# 🧪 Behavior
# Action	__name__ value	Code inside block
# python file.py	"__main__"	Runs
# import file	"file"	Does NOT run
# 📍 Use Cases

# Entry point (main())

# Testing code

# CLI scripts

# Modular project design