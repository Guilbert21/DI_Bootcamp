users = ["Mickey","Minnie","Donald","Ariel","Pluto"]
for index, name in enumerate(users, start=1):
    print(f"{index}. {name}")

for index, name in enumerate(users):
    if index == 2:
        print("")
    print(name)

sorted_users = sorted(users)
for name in sorted_users:
    print(name)

for name in users:
    if "i" in name:
        print(f"{index}. {name}")
        index += 1

index = 1
for name in users:
    if name.startswith("m") or name.startswith("p"):
        print(f"{index}. {name}")
        index += 1