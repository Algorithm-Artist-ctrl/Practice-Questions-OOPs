class Student:
    school_name = "ABC PUBLIC SCHOOL"
    default_grade = "C"  # class-level variable

    def __init__(self, name):
        self.name = name
        self.grade = Student.default_grade  # use class default

    def show_details(self):
        print(self.name, "grade is", self.grade)

    @classmethod
    def update_default_grade(cls, grade):
        cls.default_grade = grade
        print(f"Default grade updated to {cls.default_grade}")

    @staticmethod
    def check_grade(grade):
        if grade.lower() == "a":
            print("Passed")
        else:
            print("Fail")
