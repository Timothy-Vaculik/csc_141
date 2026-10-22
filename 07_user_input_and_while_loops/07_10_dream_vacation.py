# Dream Vacation
# Timothy Vaculik
# Difficulty 8tim/10

name_prompt = "What is your name? "
destination_prompt = "What is your dream vacation destination? "
more_prompt = "Would you like to let another person respond? (yes/no) "
responses = {}

while True:
    name = input(name_prompt)
    destination = input(destination_prompt)

    responses[name] = destination

    repeat = input(more_prompt)
    if repeat != 'yes':

        break

print("\n--- Dream Vacation Poll Results ---")
for name, destination in responses.items():
    print(f"{name} would like to visit {destination}.")