s = {2,4,5,6,9}

print(s," ", type(s))

# print(s[3]) #As the sets are unordered collection of items so indexing in sets doesn't make sense and thus gives error.


# SET METHODS

fruits = {"Apple" , "Mango" , "Guava"}

new_set = {1,2,3,4}

new_set.add(5)
new_set.remove(2) 
new_set.discard(4)
new_set.pop()

print(new_set)


#SET OPERATIONS

# a ={ 23, 47 , 79 , 28}
a = {24,90}
b = {24,90,80,80,47}

c = a.union(b)
print(c)

d = a.intersection(b)
print(d)

print(a.copy())

print("Returns true if all elements of set a is present in set b:",a.issubset(b))