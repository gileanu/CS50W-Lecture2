people = [
    {"name": "Razvan", "house": "here"},
    {"name": "Maria", "house": 'there'},
    {"name": "John", "house": 'anywhere'}
]

people.sort(key=lambda person : person["name"])
print(people)