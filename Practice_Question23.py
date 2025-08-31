# let me know if you have better option of doing this code
class NegativeValueError(Exception):
    pass
class BankAccount:
    def __init__(self):
        self.__balance = 50000  # private variable

    def deposit(self, amount):
        self.__balance += amount
        return f"Deposited {amount}. New Balance: {self.__balance}"

    def withdraw(self, amount):
        if amount < 0:
            raise NegativeValueError("Cannot withdraw a negative amount!")
        elif amount > self.__balance:
            print("Insufficient balance!")
        else:
            self.__balance -= amount
            print(f"Withdrawn {amount}. Remaining Balance: {self.__balance}")

    def check_balance(self):
        return f"Total Balance is: {self.__balance}"
B1 = BankAccount()
print(B1.check_balance())
print(B1.deposit(500))
try:
    B1.withdraw(-100)  # This will raise NegativeValueError
except NegativeValueError as e:
    print(f"Error: {e}")
print(B1.check_balance())
