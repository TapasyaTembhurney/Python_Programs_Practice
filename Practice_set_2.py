# 1--> Write a program that asks the user for a number and prints whether it is positive , negative , zero

num = int(input("Enter a number : "))
if (num > 0):
    print("Positive number")
elif(num < 0):
    print("Negative number")
else:
    print("Zero")

print("/n")

# 2--> Create a program that checks if a person is eligible to vote 

Age = int(input("Enter your age : "))

if (Age >= 18):
    print("You are eligible to vote.")
elif(Age <= 5):
    print("Grow Up.")
else:
    print("You are not eligible to vote.")

print("/n")

# 3--> Write a program that takes a number from the user and prints "Even" if it is even , Otherwise "Odd".

number = int(input("Enter a number : "))

if(number % 2 == 0):
    print("Even Number.")
else:
    print("Odd Number.")

print("/n")

# 4 --> Ask the user to enter a day number (1-7) and print the corresponding day of the week using match class.

day = int(input("Enter number between (1-7) : "))

match day:
    case 1:
        print("Sunday")
    case 2 : 
        print("Monday")   
    case 3 : 
        print("Tuesday")   
    case 4 : 
        print("Wednesday")   
    case 5 : 
        print("Thursday")   
    case 6 : 
        print("Friday")
    case 7 : 
        print("Saturday")
    
print("/n")

# 5--> CALCULATOR
# 
# Write a program using match case that simulates a simple calculator.
# (i) Ask the user for two numbers and an operation (+ , - , * , /).
# (ii) Perform the operation using match case.

digit1 = int(input("Enter a digit1 : "))
digit2 = int(input("Enter a digit2 : "))

operation = input("Tell What operation to be performed ?\n Addition(+) \n Subtraction(-) \n Multiplication(*) \n Division(/) \n")

match operation : 
    case "+":
        print(digit1 + digit2)
    case "-":
        print(digit1 - digit2)
    case "*":
        print(digit1 * digit2)
    case "/":
        print(digit1 / digit2)

print("/n")

# 6 --> Print numbers from 1 to 10 using a for loop

for i in range(1,11):
    print(i)
print("/n")


# 7 --> Print the multiplication table of a number(entered by user).
number3 = int(input("Enter a number : "))
for i in range (1, 11):
    print(number3 , "X" , i , "=" , number3 * i)

print("/n")

# 8 --> Calculate the sum of all the numbers from 1 to 100 using a for loop
sum = 0
for j in range(1, 101):
    sum = sum + j
print(sum)

print("/n")

#  9 --> Print following right angled star pattern.
for j in range(1,7):
        print("*" * j)
print("/n")

# 10 --> Print numbers from 1 to 10 using while Loop
m = 1
while (m < 11):
    print(m)
    m+= 1
print("/n")

# Sum of 1 to 100 numbers
sum1 = 0
l = 1
while l<=100:
    print(l)
    sum1 += l
    l += 1
print("The sum is :" ,sum1)
print("/n")

# 11 --> Write a program that keeps asking the user to enter a password until they enter a correct one.
og_password = "YKR7787"
user_password = input("Enter the password : ")
if (user_password != og_password):
    print("Wrong Password! \nEnter correct password.")
else :
    print("Successfully logged in.")

print("/n")

#  12 --> Use a while loop to reverse the given number(e.g. 123 -> 321)

number = int(input("Enter a number : "))
print(str(number)[::-1])

print("/n")

# 13 --> Use a for loop to print numbers from 1to 10 , but stop the loop if the number is 7(use break statement).

i = 1
while (i <= 10 ):
    print(i)
    if (i == 7):
        break
    i += 1

print("/n")

for y in range (1, 11):
    match y:
        case 1:
            print(1)
        case 2:
            print(2)
        case 3:
            pass
        case 4:
            print(4)
        case 5:
            print(5)
        case 6:
            print(6)
        case 7:
            print(7)
        