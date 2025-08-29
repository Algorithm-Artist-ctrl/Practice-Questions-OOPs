class Car:
    year = None  # class-level default

    def __init__(self, brand, model, year=None):
        self.brand = brand
        self.model = model
        # use provided year, or default to class-level year
        self.year = year if year is not None else Car.year
    def display(self):
        print(self.brand, self.model, self.year)
    @classmethod
    def update_year(cls, year):
        cls.year = year
