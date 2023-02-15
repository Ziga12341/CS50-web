print((lambda x, y: x + y)(5, 1))

square = lambda x: x * x

print(square(4))

people = [
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Cho", "house": "Ravenclaw"},
    {"name": "Draco", "house": "Slytherin"}
]

people.sort(key=lambda person: person["name"])
print(people)