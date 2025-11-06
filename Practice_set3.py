name = "Tapasya Tembhurney"
print(name[0])#First character
print(name[-1])#Last character
print(len(name))#length of name 

strgs1 = "Hello"
strgs2 = "World"
print(strgs1 +" " + strgs2) #concatenation of strings
#print(strgs1 , strgs2)

text = "Python Programming"
print(text[:6])
print(text[-6:])
print(text[0::2])

text2 = "Practice_set"
print(text2[-1::1])

text3 = "i love Python Programming "
print(text3.strip()) #removes extra spaces from both the ends

#Title Case
print(text3.title())

#Capitalize first character and lowercase the other characters
print(text3.capitalize())

#Count the number of o's in the text3
print(text3.count("o"))

#Check if the string is alphanumeric

strgs3 = "123abc"
if strgs3.isalnum():
    print("Yes these string is alpha numeric.")
else:
    print("These string is alphanumeric.")

#Using format create a sentence

name_1 = "Krish"
age = 20 

#Using format()
Intro = "Hello ! My name is {} and I am {} years old."
s1 = Intro.format(name_1 , age)
print(s1)
# print("Hello ! My name is {} and I am {} years old.".format(name_1, age))

#Using f-string
print(f"Hello ! My name is {name_1} and I am {age} years old.")

#STRING MANIPULATION CHALLENGE
text5 = "Coding in Python is fun."
new_text5 = text5.replace("fun", "awesome")
print(new_text5)

index = text5.index("Python")
print(index)

#Convert entire sentence into uppercase
print(new_text5.upper())

#WRITE A PROGRAM TO COUNT HOW MANY VOWELS ARE IN THE GIVEN STRING.
text5 = "Coding is Python is Fun."
sum = 0
vowels = ['a' , 'e' , 'i' , 'o' , 'u']
for char in text5.lower():
    if(char in vowels):
        sum += 1
print(f"There are {sum} vowels in the string.")


#TAKE A INPUT STRING AND CHECK IF IT IS A PALINDROME OR NOT.
str = "5554555"
# str = "BOB"
# str= "SBI"
if(str == str[::-1]):
    print("The string is Palindrome.")
else:
    print("The string is not a Palindrome.")

