# Timothy Vaculik
# Exercise 5-9: No Users
# 09/26/2026
# Difficulty 3/10
# usernames = ['timothy', 'alex', 'admin', 'mike', 'jake']
# 6/10 Difficulty

usernames = [] 

if usernames:
    for username in usernames:
        if username == 'admin':
            print("Hello admin, would you like to see a status report?")
        else:
            print (f"Hello {username} , thanks for the update for the status report!")
if not usernames:
    print ("We need some users")


