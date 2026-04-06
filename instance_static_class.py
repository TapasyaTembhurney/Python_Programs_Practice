class Employee:
    company = "HP"
    def __init__(self, name , salary):
        self.name = name
        self.salary = salary
    
    def display(self):
        info = f"The name is {self.name} and the salary is {self.salary}"

        print(info)
    
e1 = Employee("Jack" , 30000)
e2 = Employee("James" , 20000)
# print(Employee().company)
# print(Employee().name)

e1.display()