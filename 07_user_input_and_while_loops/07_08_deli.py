# deli
# Timothy Vaculik
# Difficulty 4/10

sandwich_orders = ['tuna', 'ham', 'pastrami', 'turkey', 'pastrami', 'roast beef', 'pastrami']
finished_sandwiches = []

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print(f"I made your {current_sandwich} sandwich.")
    finished_sandwiches.append(current_sandwich)

    print ("/n")
    for sandwich in finished_sandwiches:
        print(f"I made your {sandwich} sandwich.")

