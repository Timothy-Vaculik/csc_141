# Timothy Vaculik
# People and their information
# I think is is difficulty of 4/10

person_0 = {
"first_name": "Timothy",
"last_name": "Vaculik",
"age": 20,
"city": "Prague"
}

person_1 = {
"first_name": "David",
"last_name": "King",
"age": 21,
"city": "Buffalo"
}

person_2 = {
"first_name": "Nick",
"last_name": "Mele",
"age": 19,
"city": "Chicago"
}

person_3 = {
"first_name": "Sarah",
"last_name": "Johnson",
"age": 22,
"city": "Los Angeles"
}

people = [person_0, person_1, person_2, person_3]

for person in people:
    full_name = f"{person['first_name']} {person['last_name']}"
    age = person['age']
    city = person['city']
    
    print(f"Name: {full_name}, Age: {age}, City: {city}")
