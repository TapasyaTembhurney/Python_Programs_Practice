i = 1
while (i<=10):
    print(i)
    i = i+1

print("\n")

for j in range(0,21):
    
    if j == 11:
        break
    print(j)

print("\n")

for k in range(0,21):
    if k == 11:
        continue
    print(k)

print("\n")

# Pass statement is the statement which is syntatically required but no action is taken.
# n = 3
# if n == 12:
#     pass
# print (n)

for a in range (2,21):
    if a == 3:
        pass
    print(a)


class employee:
    def putdata(self):
        self.id = int(input("Enter id :"))
        self.name = input("Enter name :")
        self.rollno = int(input("Enter rollno :"))

    def display(self):
        print("Employee id:" , self.id)
        print("Employee name:" , self.name)
        print("Employee rollno:" , self.rollno)

a = employee()
a.putdata()
a.display()


from abc import ABC , abstractmethod

class Greet(ABC):
    @abstractmethod

    def say_hello(self):
        pass 
    
class English(Greet):
    def say_hello(self):
        return "Hello!"
    
new_obj = English()
print(new_obj.say_hello())
