class Student:
    def __init__(self,name,maarks):
        self.name=name
        self.marks=maarks
    def get_avg(self):
        sum=0
        for i in self.marks:
            sum+=i
        print(sum/3)

S1=Student("Karan",[18,19,18])
S1.get_avg()