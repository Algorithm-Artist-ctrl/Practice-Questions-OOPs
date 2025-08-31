class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __add__(self, other):
        m1 = self.x + other.x
        m2 = self.y + other.y
        v3 = Vector(m1, m2)
        return v3
    def __str__(self):
        return '{}i,{}j'.format (v3.x,v3.y)
v1 = Vector(2, 2)    
v2 = Vector(3, 4)     
v3 = v1 + v2   
print(v3)
print(v3.x, v3.y)    
