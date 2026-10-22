# Timothy Vaculik
# New definitions for a glossary of terms
# I think is is difficulty of 8/10

glossary = {
    'string': 'A series of characters.',
    'comment': 'A note in a program that the Python interpreter ignores.',
    'list': 'A collection of items in a particular order.',
    'loop': 'Work through a collection of items, one at a time.',
    'dictionary': "A collection of key-value pairs.",
    'function': 'A named block of code designed to do one specific job.',
    'method': 'A function that is associated with an object.',
    'argument': 'A value that is passed into a function when the function is called.',
    'parameter': 'A variable that is listed inside the parentheses in the function definition.',
    'return value': 'The value that a function returns to the calling code when it is done executing.',
    }

for word, definition in glossary.items():
    print(f"\n{word.title()}: {definition}")