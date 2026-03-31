f = open("newtext.txt" , "r")

# For binary file you will be eriting rb(read binary) or wb(write binary)

content = f.read()
print(content)

f.close()