# Timothy Vaculik
# Favorite places for many different people
# I think is is difficulty of 5/10

favorite_places = {
"Tom": ["Prague", "New York", "Paris"],
"John": ["London", "Tokyo", "Rome"],
"Sarah": ["Barcelona", "Miami", "Vienna"]
}

for name, places in favorite_places.items():
	print(f"\n{name.title()}'s favorite places are:")
	for place in places:
		print(f"- {place.title()}")