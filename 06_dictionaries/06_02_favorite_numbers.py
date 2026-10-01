# Timothy Vaculik
# Finding out favorite numbers for many different people 
# I think is is difficulty of 5/10

favorite_numbers = {
    'tim': 5,
    'nick': 59,
    'phil': 33,
    'aden': 44,
    'david': 22,
}
print(f"{favorite_numbers['aden']}') is the favorite.")
for key, value in favorite_numbers.items():
    print(f"{key}'s favorite number is {value}.")
