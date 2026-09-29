# Timothy Vaculik
# Exercise 5-9: No Users
# 09/26/2026

usernames = []
# usernames = ['timothy', 'alex', 'admin', 'mike', 'jake']

if usernames:
    for username in usernames:
        if username == "admin":
            print("Hello admin, would you want to see a status report?")
        else:
            print(f"Hello {username}, thank you for letting me see it")
else:
    print("We need to find some users!")