class Car:
    def __init__(self,brand,model,year):
        self.brand=brand
        self.model=model
        self.year=year
    def display(self):
        print(self.brand,self.model,self.year)
c1=Car("HONDA","Civic","2022")
c1.display()
