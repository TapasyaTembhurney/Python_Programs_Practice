template = "Dear {} , You are awesome. Take these {}$ bag."

a = "John"
a1 = 10000
b = "Jack"
b1 = 1000
c = "Marie"
c2 = 300

s1 = template.format(a , a1)
print(s1)

print(f"\n{s1} you are awesome and take this {a1}$ bag")

name = "Alice"
age = 30

# f-string and format string
print("\nMy name is {} and I am {} years old.".format(name, age))
print(f"\nMy name is {name} and I am {age} years old.")