class BankAcount:
    def __init__(self):
        self.__balance = 50000  # private variable

    def deposite(self, amount):
        self.__balance += amount
        return f"Deposited {amount}. New Balance: {self.__balance}"

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            return f"Withdrawn {amount}. Remaining Balance: {self.__balance}"
        else:
            return "Insufficient balance!"

    def check_Balance(self):
        return f"Total Balance is: {self.__balance}"
B1 = BankAcount()
print(B1.check_Balance())
print(B1.deposite(500))
print(B1.withdraw(100))
print(B1.check_Balance())
2