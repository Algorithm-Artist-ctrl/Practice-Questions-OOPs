class Student:
    def __init__(self,phy,maths,chem):
        self.phy=phy
        self.maths=maths
        self.chem=chem
    @property
    def calculate(self):
        self.per=str((self.phy+self.maths+self.chem)/3)+" %"
        return self.per

s=Student(97,89,90)
print(s.calculate)