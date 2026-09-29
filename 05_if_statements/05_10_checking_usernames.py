# Timothy Vaculik
# Exercise 5-10 : Checking Usernames
# Finding if there is anything wrong

current_users = ["admin", "david", "Kitty", "JOHN", "BRANDON"]

new_users = ["John", "Zach", "Brandon", "Nick", "Aden"]

current_users_lowered = [username.lower() for username in current_users]

for new_user in new_users:
    if new_user.lower() in current_users_lowered:
        print(f"{new_user} is already taken!")
        continue
    print(f"{new_user} is available!")