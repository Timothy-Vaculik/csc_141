# Timothy Vaculik
# cities and how do they relate to each other
# I think is is difficulty of 9/10

cities = {
"Prague": {
    "country": "Czech Republic",
    "population": 1_400_000,
    "fact": "Prague is famous for its historic Old Town."
},
"New York": {
    "country": "United States",
    "population": 8_300_000,
    "fact": "New York City is home to Times Square."
},
"Paris": {
    "country": "France",
    "population": 2_100_000,
    "fact": "Paris is home to the Eiffel Tower."
}
}

for city, information in cities.items():
    print(f"\nCity: {city}")


print(f"Country: {information['country']}")
print(f"Population: {information['population']}")
print(f"Fact: {information['fact']}")