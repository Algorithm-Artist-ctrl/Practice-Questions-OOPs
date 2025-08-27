class Person:
    def __init__(self,name,gender):
        self.name=name
        self.gender=gender
        print("WELCOME")
p1=Person("Tarun","Male")
print(p1.name,p1.gender)