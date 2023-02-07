sandwich_orders = ["Tuna sandwich", "Avocado sandwich", "Egg sandwich", "Sabih sandwich", "Pastrami sandwich"]
sandwich_orders.sort()
print(sandwich_orders)
finished_sandwiches = []

made = input("Enter made sanwiche:")
made = made.capitalize()

finished_sandwiches.append(made)
finished_sandwiches.sort()

if (sandwich_orders == finished_sandwiches):
    for i in range(0, len(sandwich_orders)):
        print(f"i made your {i}")

# print(finished_sandwiches)

# have some difficulties with the last 3 exercises