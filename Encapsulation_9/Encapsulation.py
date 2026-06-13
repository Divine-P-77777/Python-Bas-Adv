# Encapsulation  (3nd pillar of the oops )
# Data Hiding Public, Protected, Private
# Encapsulation is about protecting the internal data of a class. You control what the outside world can see and what it cannot. This prevents accidental modification of important data.
# Data and methods that operate on that data are bundled together inside a class
# Sensitive data is marked private so it can't be accessed directly from outside
# Access is given through controlled methods called getters anci setters
# Makes code more secure and predictable
# Real life example: ATM machine you car: check balance and withdraw, but you can't access the bank's internal system directly

class Bank:
    def __init__(self, name: str, balance: int):
        self.name = name          # Public
        self._bank_name = "SBI"   # Protected
        self.__balance = balance  # Private

    # Getter
    def get_balance(self):
        return self.__balance

    # Setter
    def set_balance(self, amount):
        if amount >= 0:
            self.__balance = amount

    def _isServerLive(self):
        return True

    def deposit(self, amount: int):
        if self._isServerLive():
            self._balance += amount
            print(f"Amount deposited, current balance = {self._balance}\n")
        else:
            print("Server is down")


    def withdraw(self, amount: int):
        if amount > self.__balance:
            print("Not enough money in bank")
        else:
            self.__balance -= amount
            print(f"Amount withdrawn, current balance = {self.__balance}")


acc = Bank("Anirudh", 1000)

acc.deposit(1000)
acc.withdraw(500)

print(acc.name)              # Public
print(acc._bank_name)        # Protected (can access, but not recommended)

print(acc.get_balance())     # Getter
acc.set_balance(5000)        # Setter
print(acc.get_balance())

print(acc.isServerLive())

# Public Variable
#     balance
#     Accessible from anywhere.

# Protected Variable
#     _balance
#     Intended for use within class and subclasses.

# Private Variable
#     __balance
#     Cannot be accessed directly outside the class.

# Getter
#     Used to read private variables.

# Setter
#     Used to update private variables safely.

# Encapsulation
#     Hides internal data and provides controlled access through methods.