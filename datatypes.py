# Integer
a = 10
b = 1
print("Intergers :",a,b)

# float
price = 10.32
print("Float :",price)


# String
str = "Say Something"
print("String :",str)

# Boolean
isMaster = True
print("Boolean :",isMaster)


# List
people = ["John", "Mary", "Mark", "Anna"]
print("List :",people)
print("List Length :",len(people))
print("List 1 Item :", people[1])

# Dictionary
person = {
    "name": "John",
    "age" : 32,
    "salary" : 12123.21
}
print("Dictionary :",person)

# Set 
A = {1,3,4,5}
B = {2,4,5,6, 7}
print("Set :",A, B)
print("Set Length :",len(A), len(B))
print("Set Union :", A.union(B))
print("Set Intersection Length :", A.intersection(B))
print("Set A subset of B :", A.issubset(B))
print("Set A superset of B :", A.issuperset(B))


# Tuples - Immutable
tup = (1,2,3,4,1)
print("Tuples :", tup)
print("Tuples length :", len(tup))
print("Tuples Count :" ,tup.count(1))