# Pizza Toppings
# Timothy Vaculik
# Difficulty 6/10

prompt = "Enter a pizza topping you want to add to your pizza (type 'quit' to finish): "
prompt += " (Enter 'quit' to exit): "
while True:
    topping = input(prompt)
    if topping.lower() == 'quit':
        break
    else:
        print(f"Adding {topping} to your pizza.")