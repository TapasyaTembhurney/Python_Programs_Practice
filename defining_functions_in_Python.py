# a = 1
# b = 2
# c = 3
# average = (a+b+c)//3 #(floor division)
# print(average)

# a1 = 7
# b1 = 3
# c1 = 7
# average1 = (a+b+c)/3.0#(normal division)
# print(average1)



#Now if want to make changes everywhere by just making changes only at one point then you can do by function.

#1
def average(a,b,c):
    #positional arguments are a , b, c
    avg = (a+b+c)//3
    # print(avg)
    return avg

o1 = average(3,4,5)
print(o1)



#2
def greet(name):
    return (f"Hello, {name}!")
print(greet("Alice"))

