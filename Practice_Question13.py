class Car:
    def __init__(self,brand,model,year):
        self.brand=brand
        self.model=model
        self.year=year
c1=Car("HONDA","Civic","2022")
print(c1.brand,c1.model,c1.year)