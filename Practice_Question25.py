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