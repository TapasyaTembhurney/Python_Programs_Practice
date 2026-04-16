class Employee:
    company = "HP"
    
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    
    def display(self):
        return f"The name is {self.name} and the salary is {self.salary}"
    
    def __str__(self): #dunder method
        return f"Employee(Name: {self.name}, Salary: {self.salary})"


# Creating object outside the class
e = Employee("Harry", 352)

print(e.name, e.salary)        # Access attributes
print(e.display())             # Call method
print(str(e))                  # Uses __str__()