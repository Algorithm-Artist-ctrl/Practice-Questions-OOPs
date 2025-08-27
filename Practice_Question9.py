class Animal:
    def makeSound(self):
        print("Some generic animal sound")

class Cat(Animal):
    def makeSound(self):
        print("Cat sound is Meow")

class Dog(Animal):
    def makeSound(self):
        print("Dog sound is Boo Boo")

a1=Animal()
a1.makeSound()
c = Cat()
c.makeSound()

d = Dog()
d.makeSound()
