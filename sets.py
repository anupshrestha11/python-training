set1 = {1, 2, 3, 4}
set2 = {2, 3, 5}

result = set1.union(set2)
print(result)

result = set1.difference(set2)
print(result)

result = set1.symmetric_difference(set2)
print(result)

result = set1.isdisjoint(set2)
print(result)

result = {1, 4}.isdisjoint({2, 3})
print(result)

result = set1.issubset(set2)
print(result)

result = {1, 2}.issubset({1, 2, 3})
print(result)

result = {1, 2}.issuperset({1, 2, 3})
print(result)

result = {1, 2, 3, 4}.issuperset({1, 2})
print(result)


print(2 in set1)
print(5 in set1)
print(5 in set2)

print(set1)
set1.discard(1) # doesnot give error if not present
print(set1)


print(set1)
set1.remove(2) # gives if not present
print(set1)
