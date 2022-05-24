#Inheritance in Object Oriented Programming
# There 3 pillars of OOP
#Inheritance, Polymorphism, Enapsulation
class Animal:

    def __init__(self,name,age,location):
        self.animal_name = name
        self.age = age
        self.location = location
    def move(self):
        print("i can move")
    
    def eat(self):
        print("i am eating")

class Fish(Animal): # Fish inherits everything from Animal and has it own unique swim()
    def swim(self):
        print("swimming yeah")


class Bird(Animal):  # Fish inherits everything from Animal and has it own unique swim()
    def fly(self):
        print("I can fly")
    
f1 = Fish("fishy",24,"Spain")
f1.swim()
f1.eat()
b1 = Bird("birdy",2,"Britain")                   