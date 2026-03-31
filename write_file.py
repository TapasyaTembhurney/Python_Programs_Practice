# Write to a file called JohnDoe.txt
# It Should contain data about JohnDoe.

f = open("JohnDoe.txt" , "w")

string_data = '''John Doe is a nice Guy. He lives in New York and has a big apartment . He Loves Python Programming and his favourite library is pandas.'''

f.write(string_data)

f.close()

