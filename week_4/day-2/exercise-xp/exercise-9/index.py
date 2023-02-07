# age = int(input("Enter your age:"))
cost = 0

while True:
    age = int(input("Enter your age and enter 0 when finished:"))
    if age == 0:
        break
if age < 3:
    cost = cost + 0
    # print("Your ticket is free")

elif age >=3 and age <=12:
    # print("the ticket is $10.")
    cost = cost + 10

elif age > 12:
    cost = cost + 15

print(f"Total cost is {cost}")



