class Student:
    school_name="ABC PUBILC SCHOOL"
    @classmethod
    def modify_schoolname(cls,name):
        cls.school_name=name
s1=Student()
print(s1.school_name)
s1.modify_schoolname("WISDOM PUBIC SCHOOL")
print(s1.school_name)
