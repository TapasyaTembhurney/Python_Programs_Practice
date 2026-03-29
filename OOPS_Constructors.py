class Employee:

    def __init__(self, salary , name , bond): #init constructor is created
        self.salary = salary #Create an instance attribute of name salary and assign it with salary
        self.name = name
        self.bond = bond

    def get_salary(self):
        return self.salary
    
    def get_info(self):
        print(f"The name of employee is {self.name}. Salary is {self.salary}. The bond is for {self.bond} years.")

e1 = Employee(120000 , "John Doe" , 4)
e1.get_info()