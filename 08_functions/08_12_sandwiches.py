# Timothy Vaculik
# sandwiches with functions
# I think is is difficulty of 7/10

def make_sandwich(*ingredients):
    """Display the ingredients of a sandwich."""
    print("Making a sandwich with the following ingredients:")
    for ingredient in ingredients:
        print(f"- {ingredient}")

        make_sandwich('ham', 'cheese', 'lettuce', 'tomato')
        make_sandwich('turkey', 'bacon', 'avocado')
        make_sandwich('peanut butter', 'jelly')