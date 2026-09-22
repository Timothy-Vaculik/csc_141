cities = ("Prerov", "Ostrava", "Brno", "Prague", "Olomouc", "Zlin", "Plzen")
print("Original list of cities:")
print(cities)

print(cities[1])
print(cities[3])
print(cities[-1])

cities_list = []
cities_list.append('Prerov')
cities_list.append('Ostrava')
cities_list.append('Brno')
cities_list.append('Prague')
cities_list.append('Olomouc')
print("\nList of cities:")
print(cities_list)

cities = ['Prerov', 'Ostrava', 'Brno', 'Prague', 'Olomouc']
cities.insert(0, 'Liberec')
print(cities)

del cities[0]
print(cities)

message = f"My first city was {cities[0].title()}."
print(message)

cities.remove("Ostrava")
print("\nList of cities after removing Ostrava:")
print(cities)

print("\nCities sorted in alphabetical order:")
print(sorted(cities))


cities = list(cities)
cities.append("Liberec")
cities.insert(0, "Brno")

print("\nModified list of cities:")
print(cities)

cities.pop(0)
print("\nList of cities after popping the first city:")
print(cities)

last_went_to = cities.pop()
print(f"\nThe last city I went to was {last_went_to.title()}.")
print("List of cities after popping the last city:")
print(cities)

cities.remove("Brno")
print("\nList of cities after removing Brno:")
print(cities)

del cities[0]
print("\nList of cities after deleting the first city:")
print(cities)

length = len(cities)
print(f"\nThe length of the modified list of cities is: {length}")  

cities.sort()
print("\nList of cities sorted in alphabetical order:")
print(cities)

cities.sort(reverse=True)
print("\nList of cities sorted in reverse alphabetical order:")
print(cities)

cities.sort()
cities.sort(reverse=True)

print(cities)
