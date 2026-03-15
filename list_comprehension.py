# Create a list containing the table of 5

# table = []

# for i in range(1 , 11):
#     table.append(5*i)

# print(table)

table = [5*i for i in range(1,11)]
print("The table for the given number is :",table)

# Square numbers

a = [2,6,8,7,9]
squared = [x**2 for x in a]
print("The squared numbers are :",squared)

# Double each number of lists

a = [1,3,4,6,8]
res = []

res = [i*2 for i in a]
print("The double of all the elements is ",res)

# Create a new list containing only even numbers from the original list a

a = [2,3,4,9,8,50]
res = [val for val in a if val % 2 == 0]
print("All the even numbers from the list are :",res)


