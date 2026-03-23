# Fixed version of Python_Collections_Practice.py
# Corrections:
# - Avoid shadowing built-ins (renamed 'list' -> 'numbers_list', 'tuple' -> 'grades_tuple')
# - Fixed case-sensitive dictionary key access ('Name', 'Grade')
# - Made set operations meaningful with different sets a and b
# - Commented out the direct tuple modification error line
# - Cleaned up minor issues for smooth execution

# --------------------------- Lists --------------------------- 

fruits = ["Apple", "Banana", "Cherry"]
print("The first fruit is:", fruits[0])

fruits[1] = "Orange"
print(fruits)
print(len(fruits))

# List comprehension and slicing
numbers_list = [i for i in range(1, 11)]
print(numbers_list)
print("The first 3 items of the list are:", numbers_list[0:3])
print("The last 3 items of the list are:", numbers_list[-3:])

print("\n")

# List methods: sort, append, remove
numbers = [5, 2, 9, 1, 7]
numbers.sort()
print("The list in ascending order is:", numbers)

numbers.sort(reverse=True)
print("The list in descending order is:", numbers)

numbers.sort()  # Reset to ascending
numbers.append(10)
print(numbers)
numbers.remove(2)
print(numbers)

# Pop, index, insert
names = ["Alice", "Bob", "Charlie"]
index = names.index("Bob")
names.pop(index)
names.insert(1, "David")
print(names)

# --------------------------- Tuples --------------------------- 

coordinates = (10, 20)
print(coordinates[0])
print(coordinates[1])

# coordinates[0] = 50  # This would raise an error - tuples are immutable

# Workaround: convert to list to modify
cor_list = list(coordinates)
cor_list[0] = 50
coordinates = tuple(cor_list)
print(coordinates)

grades_tuple = (20, 80, 89, 79, 98)
cor_list = list(grades_tuple)
cor_list[0] = 50
grades_tuple = tuple(cor_list)
print(grades_tuple)

# --------------------------- Sets --------------------------- 

my_set = {1, 2, 3, 4, 5}
print(my_set)
my_set.add(5)  # No effect - sets ignore duplicates
print(my_set)

a = {1, 2, 3}
b = {3, 4, 5}

print("Union:", a.union(b))          # {1, 2, 3, 4, 5}
print("Intersection:", a.intersection(b))  # {3}
print("Difference (a - b):", a.difference(b))  # {1, 2}

# --------------------------- Dictionaries --------------------------- 

student = {"Name": "John", "age": 20, "Grade": 'A'}
print(student)
print(student["Name"])  # Fixed: case matches key

student["Grade"] = 'A+'  # Fixed: case matches key
student["city"] = "New York"  # Added meaningful value
print(student)

my_dict = {
    "Harry": 9090909090,
    "John Doe": 99889988,
    "Donald Trump": 454545
}

print(my_dict.keys())
print(my_dict.values())

for key, value in my_dict.items():
    print(key, value)

