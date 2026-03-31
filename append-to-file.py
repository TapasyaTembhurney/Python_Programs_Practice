# Append to an existing file called JohnDoe.txt
# It Should contain data about JohnDoe.

f = open("JohnDoe.txt" , "a")

string_data = """
John Doe initially lives in Phoenix , Arizona. 
He is a very nice guy"""

f.write(string_data)

f.close()
