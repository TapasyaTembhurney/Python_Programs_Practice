class Employee:
    def __init__(self, name , salary):
        self.name = name
        self.salary= salary
    @property
    def first_name(self):
        l = self.name.split(" ")
        return l[0]

    @first_name.setter
    def first_name(self, first):
        l = self.name.split(" ")
        new_name = f"{first} {l[1]}"
        self.name = new_name

e = Employee("Jack Doe" , 34555)
# print(e.first_name())


print(e.first_name)
e.first_name = "John"
print(e.name)


class Person:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        # return getattr(self, "_name" , "Name not set")
        return self._name
    
    @name.setter
    def name(self, new_name):
        self._name = new_name

    @name.deleter
    def name(self):
        self._name = None
        # del self._name

p = Person("Alice")
print(p.name)
del p.name
print(p.name)