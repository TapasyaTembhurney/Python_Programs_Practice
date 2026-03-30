class Example:
     #Using default arguments
    def add(self , a , b =0 , c= 0):
        return a + b + c
    
obj = Example()


print(obj.add(5))
print(obj.add(5,10))
print(obj.add(4,91,29))


#Using *args to accept variable number of arguments

class Example2:
    def add1(self, *args):
        return sum(args)
    
obj = Example2()

print(obj.add1(5))
print(obj.add1(5,10))
print(obj.add1(4,91,29))
