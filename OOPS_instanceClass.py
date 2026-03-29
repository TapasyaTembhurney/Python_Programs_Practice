class Employee:
    company = "Asus" #Global Variable

    def __init__(self, salary , name , bond,company):
        #Instance attributes 

        self.salary = salary #Instance attribute of name salary and assign it with salary.
        self.name = name
        self.bond = bond
        self.company = company

    def get_salary(self):
        return self.salary
    
    def get_info(self):
        print(f"The name of the employee is {self.name} and the salary of them is {self.salary}. They have bond of {self.bond} years.")

e1 = Employee(1200, "Harris" , 7, "Tesla")
# e1.get_info()

print(e1.company) #Will always print instance attribute whenever present.
print(Employee.company) #This is class attribute

#Object Inrospection

print(dir(e1))