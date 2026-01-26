#Types of Modules in Python:
# 1) Built-in Modules
# 2) External Modules


import math
import mymodules
import requests

print(math.sqrt(110))
print(math.sqrt(81))

r = requests.get("https://www.google.com")
print(r.text)
print(r.content)

mymodules.myModule()
mymodules.Practice()