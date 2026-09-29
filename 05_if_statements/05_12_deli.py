# Timothy Vaculik
# This is aan example
# Compliant to PEP-8
# 09/26/2026
# 4/10 Difficulty

numbers = list(range(1, 10))

for number in numbers:
    if number == 1:
        ending = "st"
    elif number == 2:
        ending = "nd"
    elif number == 3:
        ending = "rd"
    else:
        ending = "th"
    print(f"{number}{ending}")

# There has to be spaces after each on because it looks messy and it is hard to read
# Spaces are put there, so people can easily see what the code is
# It won't do anything, but it will look clean