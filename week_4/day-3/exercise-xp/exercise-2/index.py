def ticket_price(age):
    if age < 3:
        return 0
    elif age >= 3 and age <= 12:
        return 10
    else:
        return 15

family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}

total_cost = 0
for member, age in family.items():
    cost = ticket_price(age)
    total_cost += cost
    print(f"{member} has to pay ${cost}")

print(f"\nTotal cost for the family is ${total_cost}")
