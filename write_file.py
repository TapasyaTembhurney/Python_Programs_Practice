# Write to a file called JohnDoe.txt
# It Should contain data about JohnDoe.

f = open("JohnDoe.txt" , "w")

# Whenever you are opening a file using write file the data will be overwritten.

# If the file doesn't exists it will create new text file and the data will be written in it but if the file exists the data will be overwritten meaning previous data will be erased . 

#  If you want the data not be erased or overwritten then use append("a") to append the data in the existing text file.


string_data = '''John Doe is a nice Guy. He lives in New York and has a big apartment . He Loves Python Programming and his favourite library is pandas.'''

f.write(string_data)

f.close()

