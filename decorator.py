#Decorator is a function that takes a function , it creates a new function inside its body(wrapper). Then it returns that new function.

def decorator(func):
    def wrapper():
        print("I am about to execute a function.")
        func()
        print("I have executed the function.")

    return wrapper

@decorator #Alternative way to write decorators used in building web applications using frameworks like flask
def say_hello():    
    print("Hello!")


say_hello()


# f = decorator(say_hello)
# print(f) #only prints object of function
# f() #calls the wrapper function

#The f() function will look like these

# def wrapper():
#         print("I am about to execute a function.")
#         print("Hello!")  #func()
#         print("I have executed the function.")