wallet = int(input("Enter amount in your wallet: $"))

items_purchase = {
  "Water": 1,
  "Bread": 3,
  "TV": 1000,
  "Fertilizer": 20
}

can_buy = []
for item, value in items_purchase.items():
    if wallet >= value:
        can_buy.append(item)

if not can_buy:
    print("Nothing")
else:
    can_buy.sort()
    print("You can afford: ", can_buy)