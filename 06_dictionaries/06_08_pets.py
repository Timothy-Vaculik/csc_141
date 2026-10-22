# Timothy Vaculik
# Pets are a fun thing to have and they can be a great companion
# I think is is difficulty of 2/10

pet1 = {
"animal": "dog",
"owner": "Tim"
}

pet2 = {
"animal": "cat",
"owner": "Nick"
}

pet3 = {
"animal": "shark",
"owner": "David"
}

pets = [pet1, pet2, pet3]

for pet in pets:
    print(f"Animal: {pet['animal'].title()}, Owner: {pet['owner'].title()}")