class Calculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
    def add(self):
        self.sum=self.num1+self.num2
        return f"Add {self.sum}"
    def subtract(self):
        self.sub=self.num1-self.sub
        return f"Subtract {self.sub}"
    def multiply(self, factor):
        self.mult=self.num1*factor
        return f"Multiply {self.mult}"
    def divide(self, divisor):
        if divisor!=0:
            self.divided=self.num1/divisor
            return f"Divide {self.divided}"
        elif divisor==0:
            print("Error: Cannot divide by zero")
            return None
        else:
            self.divided=self.num1/divisor
cal1=Calculator(12,20)
print(cal1.divide(-2))
print(cal1.multiply(3))
