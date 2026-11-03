# Timothy Vaculik
# city names with functions
# I think is is difficulty of 5/10

def city_country(city, country):
    """Return information about a city and its country."""
    return f"{city.title()}, {country.title()}"

pair_1 = city_country('Accra', 'Ghana')
pair_2 = city_country('New York', 'United States')
pair_3 = city_country('Tokyo', 'Japan')
