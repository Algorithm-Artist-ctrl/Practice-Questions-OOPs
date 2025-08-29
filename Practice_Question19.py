class MathsOperation:
    defualt_operation="+"
    def __init__(self,num1,num2):
        self.num1=num1
        self.num2=num2
    @classmethod
    def update_operation(cls,operation):
        cls.defualt_operation=operation
    @staticmethod
    def calculate(defualt_operation,num1,num2):
        if defualt_operation=="+":
            print(f"Addition of these {num1+num2}")
        elif defualt_operation=="-":
            print(f"Subtaction is {num1-num2}")
        elif defualt_operation=="/":
            print(f"Division is {num1/num2}")
        elif defualt_operation=="*":
            print(f"Multiplication is {num1*num2}")
        else:
            print("USE ONLY +,_,/,*")
m1=MathsOperation(20,40)
m1.calculate("*",30,34)