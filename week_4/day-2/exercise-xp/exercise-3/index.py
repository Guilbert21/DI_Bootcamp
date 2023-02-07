basket = ["Banana", "Apples", "Oranges", "Blueberries"]

# Remove “Banana” from the list.
basket.remove("Banana")
print(basket)

# Remove “Blueberries” from the list.
basket.remove("Blueberries")
print(basket)

# Add “Kiwi” to the end of the list.
basket.append("Kiwi")
print(basket)

# Add “Apples” to the beginning of the list.
basket.insert(0,"Apples")
print(basket)
# Count how many apples are in the basket.
apple = basket.count("Apples")
print(apple)

# Empty the basket.
basket = basket.clear()
# Print(basket)
print(basket)



