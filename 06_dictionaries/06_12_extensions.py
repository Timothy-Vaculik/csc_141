# Timothy Vaculik
# extensions for dictionaries
# I think is is difficulty of 9/10

cities = {
"Prague": {
"country": "Czech Republic",
"population": 1_400_000,
"fact": "Prague is famous for its historic Old Town.",
"language": "Czech"
},
"New York": {
"country": "United States",
"population": 8_300_000,
"fact": "New York City is home to Times Square.",
"language": "English"
},
"Paris": {
"country": "France",
"population": 2_100_000,
"fact": "Paris is home to the Eiffel Tower.",
"language": "French"
}
}

for city, information in cities.items():
    print(f"\n--- {city} ---")
    print(f"Country: {information['country']}")
    print(f"Population: {information['population']:,}")
    print(f"Language: {information['language']}")
    print(f"Interesting fact: {information['fact']}")