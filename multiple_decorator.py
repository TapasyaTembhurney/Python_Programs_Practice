def uppercase(func):
    def wrapper():
        return func().upper()
    return wrapper

def exclaim(func): 

    #function and function is created and then returned that new function with extra information is what decorators are.

    def wrapper():
        return func() + "!!!"
    
    return wrapper

@uppercase
@exclaim
def greet():
    return "helLo"

print(greet())