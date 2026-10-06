# Timothy Vaculik
# favorite numbers for many different people
# I think is is difficulty of 1/10

favorite_numbers = {
"Tim": [7, 17, 23],
"John": [1, 4, 13],
"Sarah": [66, 22, 54]

}

for name, numbers in favorite_numbers.items():
    print(f"{name}'s favorite numbers are:")
for number in numbers:
    print(number)