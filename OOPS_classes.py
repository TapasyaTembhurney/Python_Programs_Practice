# class : Class is a blueprint or a template. EG. Form for an exam that contains name , age , electives , father's name etc.
# Object : Spcific instance created from the template(class). Eg. Form which contains data from John Doe.


class Employee:
    def get_salary(self):  #Function
        
        '''Self is mandatory parameter it is the parameter that is used to reference the object of the class which is being created.'''

        return 120000
    
e = Employee() #Object of a class Employee is created here.
print(e.get_salary()) #Employee e's get_salary method/function is called.