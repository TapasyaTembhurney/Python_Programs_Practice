class Employee:
    company = "HP"
    def __init__(self, name , salary):
        self.name = name
        self.salary = salary
    
    def display(self):
        info = f"The name is {self.name} and the salary is {self.salary}"
    def display(self):
        info = f"The name is {self.name} and the salary is {self.salary}"
        
    e = Employee("Harry", 352)
    print(e.name , e.salary)
    print(str(e))
