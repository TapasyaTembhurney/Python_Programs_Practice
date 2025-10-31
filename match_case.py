a = int(input("Enter a number : "))

match a :
    case 1:
        print("You have won a Laptop !!!")
    case 2 :
        print("You have won a Mobile !")
    case 3 :
        print("You have won a Cosmetics hamper.")
    case _:
        print("Better luck next time")
        