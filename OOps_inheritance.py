class Animal: #Parent class
    
    location = "Australia"

    def __init__(self, name):  
        self.name = name

    def speak(self):
        print("Speaking Now ...")

class Dog(Animal): #This is how inheritance is done in Python
    def speak(self):
        super().speak() # We are using speak function of the parent class.
        print("Woof!")

a = Animal("Jessy")
a.speak()

d = Dog("Bruno")
d.speak()
print(d.location)   
