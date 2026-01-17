def add(a, b):
    sum = a+b
    return sum

c = add(3,6)
print(c)

#Here a and b in function are parameters and 3,6 in function calling are arguments which is being passed for computaional process.

#And (a,b) are positional arguments

#And (a,b,plus = 0 ) HERE plus = 0 is default argument but if you give the plus parameter as positional argument then it will error [like (a,b,plus) will give an error]. 
# Default values are placed at the very end or after all  the parameters.

def Student(name , age):
    print(f"Name: {name} and Age : {age}")

Student(age = 20 , name = "Tapasya")

def add(d,e,plus=0):
    sum = d+e+plus
    return sum

func_call = add(3,7)
print(func_call)

#Keyword Arguments
def Students(a1 , b1):
    sum1 = a1 + b1
    return sum1

    # print(f"Num1: {a1} , Num2:{b1}")
call = Students(b1= 7, a1= 4)
print(call)



