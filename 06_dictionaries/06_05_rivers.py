# Timothy Vaculik
# Rivers of the Earth
# I think is is difficulty of 4/10

rivers = {
    'nile': 'egypt',
    'mississippi': 'united states',
    'colorado ': 'colorado ',
    }

print("\n---River Sentences---")
for river, country in rivers.items():
    print(f"The {river.title()} flows through {country.title()}.")

print("\n---Rivers---")
for river in rivers.keys():
    print(f"- {river.title()}")

print("\n---Countries---")
for country in rivers.values():
    print(f"- {country.title()}")