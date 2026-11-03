# Timothy Vaculik
# user profile with functions
# I think is is difficulty of 3/10


def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info


user_profile = build_profile(
    'timothy', 
    'vaculik',
    location='philadelphia',
    field='cybersecurity',
    language='python'
)
print(user_profile)