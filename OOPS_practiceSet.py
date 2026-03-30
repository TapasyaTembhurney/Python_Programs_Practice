'''Create a class Car with a method drive() that prints "Car is moving".
Create a object of car and call drive().'''

class Car:
    def drive(self):
        print("Car is moving")

car = Car()
car.drive()

'''Create a class Person with a constructor (__init__) that accepts name and age as arguments and stores them as instance attributes.
Create an object and print the person's name and age.'''

class Person:
    def __init__(self, name , age):
        
        #Instance Attributes

        self.name = name
        self.age = age

    def display(self):
        print(f"The name of the person is {self.name} and age of them is {self.age}.")


person = Person("Mahi" , "38")
print(person.name , person.age) #Using object

person.display() #Using a method

"""Create a base class Animal with a method sound() that prints "some sound".
Create a derived class Dog that overrides sound() to print "Bark!" .
Create a object of Dog and call sound()."""

#METHOD OVERRIDING - "sound() method overriden"
class Animal:
    def sound(self):
        print("Some sound !")

class Dog(Animal):
    def sound(self):
        print("Bark!")

a = Animal()
a.sound()

dog = Dog()
dog.sound()