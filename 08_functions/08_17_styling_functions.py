# Timothy Vaculik
# importing functions
# I think is is difficulty of 8/10

"""08_02_favorite_book"""

def favorite_book(title):
    """Display a message about a favorite book."""
    print(f"One of my favorite books is {title}.")


favorite_book("The Great Gatsby")

"""08_03_tshirt"""

def make_shirt(size="Large", message="I love Python"):
    """Display information about a t-shirt."""
    print(f"The shirt is {size} and the message is {message}.")
    print(f"It will have this message: {message}")


make_shirt()

"""08_04_large_tshirt"""

def city_country(city, country):
    """Return information about a city and its country."""
    return f"{city.title()}, {country.title()}"

pair_1 = city_country('Accra', 'Ghana')
pair_2 = city_country('New York', 'United States')
pair_3 = city_country('Tokyo', 'Japan')
