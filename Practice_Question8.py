class Rectangel:
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
    def area(self):
        return f"Area of Rectangle = {self.length*self.breadth}"
    def perimeter(self):
        p=(self.length+self.breadth)
        return f"Perimeter of Rectange is {2*p}"
r1=Rectangel(8,6)
print(f"{r1.area()} and {r1.perimeter()}")


    