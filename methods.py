def greeting(name):
    print(f"Hi, {name}")


greeting("Anup")


nameList = ["John", "Jane", "Micheal", "Rose"]
for name in nameList:
    greeting(name)


def add(a, b):
    return a + b


print(add("John", "John"))
print(add(1, 2))
print(add(True, True))
print(add(False, False))
print(add(False, True))


# find squareroot
from math import sqrt
def  find_squareroot():
    val = eval(input('Enter number: '))
    result = sqrt(val)
    print(f"Square-root of {val} is {result}")

find_squareroot()

