class Employee:
    def __init__(self):
        self.__salary=50000
    def set_salary(self,amount):
        self.__salary+=amount
        print(f"The salary after updating is {self.__salary}")
    def get_salary(self):
        print("Present salary",self.__salary) 
e1=Employee()
e1.set_salary(20000)
e1.get_salary()