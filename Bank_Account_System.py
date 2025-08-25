class BankAccount:
    Bank_Name="ABC_Bank"
    def __init__(self, account_holder, initial_balance):
        self.account_holder=account_holder
        self.initial_balance=initial_balance
    def withdrow(self,amount):
        self.initial_balance-=amount
        print(f"{amount}  debited from your Account")
        print(f"Available Balance is {self.aval_balance()}")
    def deposite(self,amount):
        self.initial_balance+=amount
        print(f"{amount} credited in to your account")
        print(f"Available Balance is {self.aval_balance()}")
    def aval_balance(self):
        return self.initial_balance
acc1=BankAccount("Tarun",20000)
acc1.deposite(500)
acc1.withdrow(1000)
print(acc1.aval_balance())