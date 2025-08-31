'''Create a class Person with an attribute name and a method greet.

Create another class Employee with an attribute job_title.

Create a subclass Manager that inherits from both Person and Employee.

Instantiate an object of Manager and call both greet and job_title.'''
class Person:
    def __init__(self,name):
        self.name=name
    def greet(self):
        print(f"Hello {self.name}")
class Employee:
    def __init__(self,job_tittle):
        self.job_tittle=job_tittle
    def title(self):
        print(f"Job Tittle is {self.job_tittle}")
class Manager (Person,Employee):
    def __init__(self,name,job_tittle):
        Person.__init__(self,name)
        Employee.__init__(self,job_tittle)
obj=Manager("Alogrithm-Artist-Ctrl","Coder")
obj.greet()
obj.title()