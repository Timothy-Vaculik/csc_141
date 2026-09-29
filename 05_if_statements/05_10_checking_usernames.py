# Timothy Vaculik
# Checking Usernames
# Finding if there is anything wrong
# 09/26/2026

current_users = ['admin', 'Phil', 'Zack', 'Pam', 'Zach']
new_users = ['Rose', 'David', 'Aden', 'Emily', 'Tim']

current_users_lower = [user.lower() for user in current_users]

for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print(f"The username '{new_user}' is already taken. Please enter a new username.")
else:
    print(f"The username '{new_user}' is available.")
