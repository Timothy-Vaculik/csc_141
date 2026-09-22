pizzas = ["Veggie Delight", "Peperoni", "Jimmys Pie", "Anchovies", "Cheese"]

for pizza in pizzas:
    print(pizza)

    print("Damn, I want some that " + pizza + "!")
print("Loop is done!")

friend_pizzas = pizzas[:]

pizzas.append('hawaiian')

friend_pizzas.append('mushroom')


print("My favorite pizzas are:")

for pizza in pizzas:
    print(pizza)