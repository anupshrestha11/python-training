person = {
    "name": "John Doe",
    "age": 32,
    "isMarried": False,
    "salary": 20000.00
}

print(person)

print(person['name'])
print(person.get('age', 'not known'))
print(person.get('birthday', 'not known'))

print(person.values())

person['birthday'] = "1990-01-01"
print(person)

person.pop("name")
print(person)

person.popitem()
print(person)

new_data = {
    "guardian" : "Mary Doe"
}

person.update(new_data)
print(person)

person.clear()
print(person)
