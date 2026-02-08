def Sum(a,b):
    add = a + b
    z = 1 #local variable
    return add

def multiply(a,b):
    mul = a * b
    z = 32 #local variable
    return mul

z = 9 #Global variable

print(z)

print("\n")

print(Sum(6,9))

print(multiply(7,8),"\t", end="")

print(z)

# --------------------------------

# Use of Global variables 

def Sum1(c,d):

    '''This is Sum function '''

    print("The Sum of two numbers is - ")
    add = c + d
    global z #Please modify global z
    z = 0 #This will refer to global z and not create a local variable.
    return add 

z = 3 

print(Sum1.__doc__)
print(Sum1(3,4))
print(z)


# ----------(Doctsring)-------------------
 
def factorial(num):
    '''This function is used for finding factorial of numbers'''

    if num == 0 or num == 1:
        return 1
    else:
        fact = 1
        for i in range(num ,0 , -1):
            fact = fact * i 
  
    return fact

print(factorial.__doc__)
print(factorial(5))

# Note -> YOU CAN ALSO WRITE MULTILINE DOCSTRING.