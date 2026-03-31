import os

a = os.listdir("dir")

print(a)
print(os.getcwd())


print(os.path.exists("dir")) # dir is a directory . Therefore True.
print(os.path.exists("newtext")) # newtext is a text file not a directory . Therefore False

# os.remove(dir) # gives error as os.remove() doesn't remove directories. It just removes files.

os.remove("sample.txt") #Removed sample.txt file 