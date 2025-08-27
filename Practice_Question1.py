class Circle:
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        r=(22/7)*self.radius*self.radius
        return f"Area = {r}"
    def perimeter(self):
        p=2*(22/7)*self.radius
        return f"Perimeter = {p}"
c1=Circle(5)
print(c1.area())
print(c1.perimeter())
