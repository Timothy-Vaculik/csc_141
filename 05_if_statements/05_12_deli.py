# Timothy Vaculik
# This is aan example
# Compliant to PEP-8
# 09/26/2026

nums = list(range(1, 10))
print(nums)

ending = ""
for num in nums:

    if num == 1:
        ending = "st"
    elif num == 2:
        ending = "nd"
    elif num == 3:
        ending = "rd"
    else:
        ending = "th"
    print(f"{num}{ending}")

# There has to be spaces after each on because it looks messy and it is hard to read
# Spaces are put there, so people can easily see what the code is
# It won't do anything, but it will look clean