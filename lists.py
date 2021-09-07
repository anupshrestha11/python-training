numbers = [2, 5, 1, 3, 8, 7, 10, 9, 4, 6]
print(numbers)
print(len(numbers))
print(numbers[1])
print(numbers.index(5))

numbers.sort()
print(numbers)

numbers.reverse()
print(numbers)


numbers.remove(5)
print(numbers)

numbers.append(5)
print(numbers)

numbers.pop()
print(numbers)

numbers.insert(1, 0)
print(numbers)

numbers.extend(['a','b'])
print(numbers)
