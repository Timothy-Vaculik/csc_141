# Timothy Vaculik
# Exercise 5-6 : Stages of Life
# What age in life is this person

age = 50

if age < 2:
    print("The person is a baby.")
elif age in range (2,4):
    print("The person is a toddler.")
elif age in range (4,13):
    print("The person is a kid.")
elif age >= 13 and age < 20:
    print("The person is a teenager.")
elif age >= 20 and age < 65:
    print("The person is an adult.")
else:
    print("The person is an elder.")