a = (3,2,4,2,9)

print(a)

print(a[1])

# a[3] = 32 [New item assignment is not allowed in tuple.]
# print(a)

single_element = (5,) #In Python for creating tuple always write comma(,) after the element in python otherwise it will treat it as single integer.
print(single_element)

tp = (3, 2, 10)

a , b , c = tp
print("The tuple unpacking gives :",a,b,c)

t = (30, 90, 20, 80, 79, 220, 20)

print(t.index(20))
print(t.count(79))   