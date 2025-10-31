i = 1
while (i<=10):
    print(i)
    i = i+1

print("\n")

for j in range(0,21):
    
    if j == 11:
        break
    print(j)

print("\n")

for k in range(0,21):
    if k == 11:
        continue
    print(k)

print("\n")

# Pass statement is the statement which is syntatically required but no action is taken.
# n = 3
# if n == 12:
#     pass
# print (n)

for a in range (2,21):
    if a == 3:
        pass
    print(a)