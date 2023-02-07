# my_fav_numbers = set({"21", "4", "30"})
# print(my_fav_numbers)

# my_fav_numbers.add("13")
# my_fav_numbers.add("14")
# print(my_fav_numbers)

# my_fav_numbers.pop(-1)
# print(my_fav_numbers)

# Create a set called my_fav_numbers with all your favorites numbers.
my_fav_numbers = set((12, 21, 13))
print(my_fav_numbers)

# Add two new numbers to the set.
my_fav_numbers.add(4)
my_fav_numbers.add(5)
print(my_fav_numbers)

# Remove the last number.
my_fav_numbers.remove(5)
print(my_fav_numbers)

# Create a set called friend_fav_numbers with your friend’s favorites numbers.
friend_fav_numbers = set((56, 40, 23))
print(friend_fav_numbers)

# Concatenate my_fav_numbers and friend_fav_numbers to a new variable called our_fav_numbers.
our_fav_numbers = my_fav_numbers.union(friend_fav_numbers)
print(sorted(our_fav_numbers))
