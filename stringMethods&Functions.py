# Strings are immutable(Non-changeable)
string1 = "Tapasya"

# string1[0] = "S" #You cannot do these

a = len(string1) #length of string by len() function
print(a)

print("\n")
# Changing Case
text = "Python Programming"

print("\tOUTPUT" , "\t   ||" , "\tOriginal Input")
print(text.upper() ,"||",  text) #PYTHON PROGRAMMING
print(text.lower(), "||", text) #python programming
print(text.title(), "||" , text)#Python Programming
print(text.capitalize(), "||" , text) #Python programming

print("\n")

#REMOVING WHITESPACE
text1 = " Welcome to Python Programming "
print(text1.strip()) #Removes space from front and end
print(text1.lstrip()) #Left strip
print(text1.rstrip()) #Right strip

#FINDING AND REPLACING
text2 = "Python is Fun"
print(text2.find("is"))
print(text2.replace("Fun" , "awesome."))

# Splitting and Joining
text3 = "Apple,Banana,Orange" #splitting the string by comma means we want to create a list out of it. 
fruits = text3.split(",") #String to List
print(fruits)
print(",".join(['Apple','Banana','Orange'])) # List to string


print("\n")

#CHECKING STRING PROPERTIES
text = "Python123"
print(text.isalpha())  # Output: False
print(text.isdigit())  # Output: False
print(text.isalnum())  # Output: True
print(text.isspace())  # Output: False