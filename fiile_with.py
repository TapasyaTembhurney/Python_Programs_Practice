# f = open("newtext.txt" , "r")
# content = f.read()
# print(content)
# f.close()

# Alternate to above code using with statement.


with open("newtext.txt" , "r") as f:
    content = f.read()
    print(content)

    #No need to write f.close() because file already closed by default when using with syntax.