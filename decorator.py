#Decorator is a function that takes a function , it creates a new function inside its body(wrapper). Then it returns that new function.

def decorator(func):
    def wrapper():
        print("I am about to execute a function.")
        func()
        print("I have executed the function.")

    return wrapper

def say_hello():    
    print("Hello!")

f = decorator(say_hello)
# print(f) #only prints object of function
f() #calls the wrapper function

#The f() function will look like these

# def wrapper():
#         print("I am about to execute a function.")
#         print("Hello!")  #func()
#         print("I have executed the function.")