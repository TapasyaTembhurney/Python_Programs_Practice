marks = {"Harry" : 34, "Jack" : 44 , "Sia" : 32}

print(marks , type(marks))

print("\n")
print(marks["Harry"])
print(marks["Sia"])

marks["Harry"] = 3 # Updation in dictionary
print(marks)

# ----------------------------------------------------

# DICTIONARY METHODS

print(marks.keys()) #Gives all the keys in o/p
print(marks.values()) #Gives all the values of keys in o/p

marks.pop("Sia" , "Harry") 
# marks.clear()
print(marks)

v = marks.pop("Sia" , "Harry") 
# marks.clear()
print(v)

print("The copy of the marks dictionary is :",marks.copy())

print(marks.fromkeys("Hampi"))

print(marks.get("Harry"))

print(marks.items())

# print(marks.popitem())

upd_dictionary = marks.setdefault('Taylor', 99)
print(upd_dictionary)

print(marks)

# ----------------------------------------------------------

# DICTIONARY COMPREHENSION
table_of_5 = {i : 5*i for i in range(1,11)}
print(table_of_5)

