# movie tickets
# Timothy Vaculik
# Difficulty 5/10

prompt = "/n How old are you?"
prompt += " (Enter 'quit' to exit): "
while True:
    age = input(prompt)
    if age.lower() == 'quit':
        break
    age = int(age)
    if age < 3:
        print("Your ticket is free.")
    elif age < 12:
        print("Your ticket is $10.")
    else:
        print("Your ticket is $15.")