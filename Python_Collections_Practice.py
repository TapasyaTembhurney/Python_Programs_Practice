fruits = ["Apple" , "Banana" , "Cherry"]

print("The first fruit is :",fruits[0])

fruits[1] = "Orange"
print(fruits)

print(len(fruits))

# ---------------------------

# CREATE A LIST OF NUMBERS FROM 1 TO 10

list = [i for i in range(1,11)]
print(list)
print("The first 3 items of the list are:",list[0:3])
print("The last 3 items of the list are:",list[-3:])

print("\n")
# --------------------------------------------

#LIST METHODS

numbers = [5, 2, 9, 1, 7]

numbers.sort()
print("The list in ascending order is :",numbers)

numbers.sort(reverse = True)
print("The list in descending order is :",numbers)

#Append
numbers.sort()
numbers.append(10)
print(numbers)
numbers.remove(2)
print(numbers)

# ---------------------------------
# LIST METHODS

names = ["Alice" , "Bob" , "Charlie"]

index = names.index("Bob")  # find position of Bob
names.pop(index)            # remove Bob
names.insert(1, "David") # insert David at same position

print(names)

# --------------------------------------------
# TUPLES AND OPERATIONS ON TUPLES

coordinates = (10 , 20)
print(coordinates[0])
print(coordinates[1])

# coordinates[0] = 50
# print(coordinates) #As tuples are immutable

corlist = list(coordinates)
corlist[0] = 50  
coordinates = tuple(corlist)
print(coordinates)

tuple = (20 , 80 , 89, 79, 98)

corlist = list(tuple)
corlist[0] = 50
coordinates = tuple(corlist)
print(tuple)

# ------------------------------

# SETS AND ITS METHODS

my_set = {1,2,3,4,5}

print(my_set)
my_set.add(5)

a = {1,2,3}
b = {3,4,5}

union = b.union(b)
intersection = b.intersection(b)
difference = b.difference(b)

# ---------------------------------

# DICTIONARY AND ITS METHODS

student = {"Name":"John" , "age":20 , "Grade":'A'}
print(student)

print(student['name'])

student['grade'] = 'A+'
student['city'] = 'A+'


my_dict = {
    "Harry" : 9090909090,
    "John Doe" : 99889988,
    "Donald Trump" : 454545
}

print(my_dict.keys())
print(my_dict.values())

for key , value in my_dict.items():
    print(key , value)