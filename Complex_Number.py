class ComplexNumber:
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary
    def __add__(self, other):
        new_real = self.real + other.real
        new_imaginary = self.imaginary + other.imaginary
        return ComplexNumber(new_real, new_imaginary)
    def subtract(self, other):
        new_real = self.real - other.real
        new_imaginary = self.imaginary - other.imaginary
        return ComplexNumber(new_real, new_imaginary)
    def multiply(self, other):
        new_real = self.real * other.real - self.imaginary * other.imaginary
        new_imaginary = self.real * other.imaginary + self.imaginary * other.real
        return ComplexNumber(new_real, new_imaginary)
    def showNumber(self):
        sign = '+' if self.imaginary >= 0 else '-'
        print(f"{self.real} {sign} {abs(self.imaginary)}i")
num1 = ComplexNumber(10, 2)
num2 = ComplexNumber(1, 2)
print("Addition:")
sum_result = num1 + num2
sum_result.showNumber()
print("Subtraction:")
sub_result = num1.subtract(num2)
sub_result.showNumber()
print("Multiplication:")
mul_result = num1.multiply(num2)
mul_result.showNumber()
