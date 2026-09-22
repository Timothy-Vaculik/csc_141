guests = ["Drake", "Morgan Wallen", "Luke Bryan", "Madonna", "kanye West", "Taylor Swift", "Beyonce"]

print(f"I'm sorry guys, but only two people can come to dinner.")

shrink_guest = guests.pop(0)
print(f"I'm sorry {shrink_guest.title()}, but you can't come to dinner.")

shrink_guest = guests.pop(1)
print(f"I'm sorry {shrink_guest.title()}, but you can't come to dinner.")

shrink_guest = guests.pop(2)
print(f"I'm sorry {shrink_guest.title()}, but you can't come to dinner.")

shrink_guest = guests.pop(3)
print(f"I'm sorry {shrink_guest.title()}, but you can't come to dinner.")

print(f"Hey {guests[0].title()} and {guests[1].title()}, you are still invited to dinner.")

del guests[0]
del guests[1]

print(guests)