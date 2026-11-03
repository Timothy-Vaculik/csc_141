"""Timothy Vaculik
Large t-shirt
Difficutly 3/10"""


def make_shirt(size="Large", message="I love Python"):
    """Display the size and message for a shirt."""
    print(f"I'm going to make a {size} t-shirt.")
    print(f'The message on the shirt will be: "{message}"')


make_shirt()
make_shirt("Medium")
make_shirt("Small", "Python is fun")