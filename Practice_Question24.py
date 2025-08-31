#MRO----->(Method Resolution Odrer)
class A:
    def show1(self):
        print("Feature 1 A in show ")
class B(A):
    def show2(self):
        print("Feature 2 B in show")
class C(B):
    def show3(self):
        print("Feature 3 C in show")
c1=B()
c1.show1()
c1.show2()
c2=C()
c2.show1()
c2.show2()
c2.show3()
