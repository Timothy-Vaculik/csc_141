# Timothy Vaculik
#  Polling for favorite languages
# I think is is difficulty of 6/10

poll = ["tim", "nick", "phil", "aden", "david", "erin"]

favorite_languages = {
    'tim': 'python',
    'nick': 'java',
    'phil': 'c++',
    'aden': 'python',
    'david': 'java',

}

for person in poll:
    if person in favorite_languages.keys():
        print(f"Thank you for taking the poll, {person.title()}!")
    else:
        print(f"{person.title()}, please take the poll!")