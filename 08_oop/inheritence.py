# Inheritance means one class can reuse attributes and methods from another class.

class Animal:

    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating")


class Dog(Animal):

    def bark(self):
        print(f"{self.name} says Woof!")

dog = Dog("Buddy")    

dog.eat()  # Inherited method from Animal class
dog.bark()  # Method from Dog class
