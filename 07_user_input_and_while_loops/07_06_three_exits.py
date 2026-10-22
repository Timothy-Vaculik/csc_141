# Three Exits
# Timothy Vaculik
# Difficulty 8/10

prompt = "Enter a pizza topping you want to add to your pizza (type 'quit' to finish): "
prompt += " (Enter 'quit' to exit): "


active = True
topping = ""
while active:
    topping = input(prompt)

    if topping == 'quit':
        active = False
    else:
        print(f"Adding {topping} to your pizza.")



        prompt = "Enter a pizza topping you want to add to your pizza (type 'quit' to finish): "
prompt += " (Enter 'quit' to exit): "


prompt = "\nEnter a pizza topping you'd like to add: "
prompt += "\n(Enter 'quit' when you are finished) "

topping = ""
while topping != 'quit':
    topping = input(prompt)

    if topping != 'quit':
        print(f"Adding {topping} to your pizza.")


prompt = "\nEnter a pizza topping you'd like to add: "
prompt += "\n(Enter 'quit' when you are finished) "
while True:
    topping = input(prompt)

    if topping == 'quit':
        break
    else:
        print(f"Adding {topping} to your pizza.")


