class Father:
    def __init__(self,father_name):
        self.father_name=father_name
class Mother:
    def __init__(self,mother_name):
        self.mother_name=mother_name
class Child(Father,Mother):
    def __init__(self, child_name,father_name,mother_name):
        self.child_name=child_name
        Father.__init__(self,father_name)
        Mother.__init__(self,mother_name)
c3=Child("HARSH","HARISH CHANDRA","LALITA")
print(c3.child_name,c3.father_name,c3.mother_name)
print(c3.father_name)
print(c3.mother_name)
