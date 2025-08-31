class Circle:
    def __init__(self,radius):
        self.radius=radius
class Rectangle:
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
class Calling(Circle,Rectangle):
    def __init__(self,radius,length,breadth):
        print("VALUES OF CIRCLE AND RECTANGLE")
        Circle.__init__(self,radius)
        Rectangle.__init__(self,length,breadth)
    def calculate_area(self):
        self.area_circle=3.14*(self.radius**2)
        self.area_rectangle=self.breadth*self.length
        print(f"Area of circle is {self.area_circle}")
        print(f"area of rectangle is {self.area_rectangle}")
obj=Calling(2.2,12,10)
obj.calculate_area()
            

