import argparse

parser = argparse.ArgumentParser(description= "Simple Calculator")

parser.add_argument("num1", type = float , help = "First Number") 
parser.add_argument("num2", type = float , help = "Second Number") 
parser.add_argument("operations", choices = ["Add","Sub", "Mul", "Div"] , help = "Operations to be performed")

args = parser.parse_args()

print(args) 

if(args.operations == "Add"):
    print(f"The result is {args.num1 + args.num2}")
elif(args.operations == "Sub"):
    print(f"The result is {args.num1 - args.num2}")
elif(args.operations == "Mul"):
    print(f"The result is {args.num1 * args.num2}")
elif(args.operations == "Div"):
    print(f"The result is {args.num1 / args.num2}")
else:
    print("Some error occured")

