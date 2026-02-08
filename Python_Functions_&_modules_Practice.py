#TASK 1 -> (i) Write a function greet() that prints "Hello, Python Learner!" when called. 

def greet():
    print("Hello, Python Learner!")

greet()

# (ii) Write a function square(num) that returns the square of a given number. Test it with different numbers.

def square(num):
    sqr = num * num
    return sqr

print(square(3))
print(square(4))
print(square(7))
print(square(9))
print(square(10))

# -----------------------------------------

# TASK 2 -> FUNCTION ARGUMENTS & RETURN VALUES

# (i) Write a function full_name(first , last) that takes first name and last name as parameters and returns a single string in a format "First Last" .

# def full_name(first , last):
#     print(first + " " + last)

# full_name('James' , 'Watson')

def full_name(first , last):
   return f"{first} {last}"

print(full_name('James', 'Watson'))

# (ii) Write a function calculate_area(length , width = 10) that returns the area of a rectangle .Test it by calling the function with:
       # 1. Both Length and Width
       # 2. Only length (use default width)


def calculate_area(length , width = 10):
    area_of_rec = length * width 
    return area_of_rec

# def calculate_area(length , width = 10):
    # return length * width

# 1. 
print(f'The Area of Rectangle is {calculate_area(20, 10)}')

#2. 
print(calculate_area(70))

# ----------------------------------------

# TASK-3 -> LAMBDA FUNCTIONS

# 1. Write a lambda function that adds two numbers and test it.

add = lambda num1 , num2 : num1 + num2

print(add(3 , 5))
print(add(7 , 9))

# 2. Create a list [1,2,3,4,5] and use map() with a lambda function to find their squares.

squares = lambda x : x * x
list1 = [1 , 2 , 3 , 4 , 5]

result = list(map(squares , list1))
print(f'These are the square of the elements of list : ', result)

# --------------------------------------------------------------------

# TASK-3 -> RECURSION IN PYTHON

# 1. Write a recursive function "factorial(n)" that returns the factorial of a number.
# 2. Write a recusrive function "sum_of_digits(n)" that return the sum of all the digits of a given number.

# 1. 

def factorial(n):

    if n == 0 or n == 1:
        return 1
    
    else: 
        fact = 1
        for i in range(n,0,-1):
            fact = fact * i     
    return fact    

print(factorial(5))

# 2.
def sum_of_digits(n):
    add = 0 
    while n > 0:
        digit = n % 10
        add = add + digit
        n = n // 10

    return add

print(f"The sum of all the digits of the given number is :", sum_of_digits(24))
print(f"The sum of all the digits of the given number is :", sum_of_digits(36))
print(f"The sum of all the digits of the given number is :", sum_of_digits(3632))

# --------------------------------------------------------------------------------------

# TASK 5 -> MODULES AND PIP - USING EXTERNAL LIBRARIES
 
# 1. IMPORT MATH MODULE AND USE IT TO :
#   (I) FIND THE SQUARE ROOT OF 144
#   (II) CALCULATE SIN(90)
 
# 2. INSTALL AND IMPORT THE REQUESTS MODULE(IF AVAILABLE) AND USE IT TO FETCH DATA FROM "http://api.github.com" .

# 1.(I)
import math

print(math.sqrt(144))

print(math.sin(math.radians(90)))

# 2.
import requests #pip install requests

a = requests.get("http://api.github.com")
print(a.json())

# --------------------------------------------------

# TASK - 6 -> VARIABLE SCOPE AND DOCSTRINGS

# 1. WRITE A FUNCTION INCREMENT() THAT HAS A LOCAL VARIABLE COUNTER INITILIASED TO 0 AND INCREMENTS TO 1 EACH TIME IT IS CALLED . OBSERVE WHETHER THE VALUE PERSISTS ACROSS FUNCTION CALLS.
# 2. WRITE A FUNCTION MULTIPLY(a,b) THAT HAS A PROPER DOCSTRING EXPLAINING WHAT IT DOES.THEN USE HELP(MULTIPLY) TO DISPLAY THE DOCSTRING .

# 1.
def increment():
    counter = 0 
    counter = counter + 1
    print(counter)

increment()
increment()
increment()
increment()
increment()

# 2. 
def multiply(a,b):
    '''
    Multiply function is used to multiply the two numbers.  

    Parameters:
            a(integer or float datatype): The first number. 
            b(integer or float datatype): The second number. 
    
    Returns :
            int or float : The product of a and b.
    '''

    mul = a * b
    return mul

print(f"The Multiplication of two numbers is :",{multiply(3,5)})

help(multiply) #Used to give the docstring description in the output.

# ---------------------------------------------------------------------

# TASK-7 -> BONUS CHALLENGES

# 1. Write a recsursive function fibonacci(n) that prints the first n fibonacci numbers.
# 2. Write a function safe_divide(a,b) that returns the results as a/ b, but returns "Cannot divide by zero" if b = 0
# 3. Create a small my_utils.py module and with a function is_even(n) that returns True if n is even . Import and use it in another python file. 


# 1.

def fibonacci(n1):
    if n1 <= 1:
        return n1 
    
    else:
        return fibonacci(n1-1) + fibonacci(n1-2)
    
terms = int(input("Enter a number : "))

for i in range(terms):
    print(fibonacci(i) , end = " ")
    
print("\n")
# 2.

def safe_divide(a,b):
    if b == 0:
        return "Cannot be divided my zero"
    
    else:
        divide = a / b
        return divide
    
print(safe_divide(4,2))
print(safe_divide(3,0))

print('\n')


# 3.
import my_utils

n2 = int(input("Enter a number : "))

if my_utils.is_even(n2):
    print("Even")

else:
    print("Odd")

