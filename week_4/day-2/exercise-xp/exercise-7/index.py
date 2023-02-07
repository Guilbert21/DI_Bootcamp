fruits = input("Enter your favourite fruit(s) 'use single space between each fruit'")
print(type(fruits))

fruits_to_list = fruits.split()
print(type(fruits_to_list))
# print(fruits_to_list)

another = input("Enter another fruit: ")
fruits_to_list.append(another)

match = fruits_to_list.count(another)
if match == 2:
    print("You chose one of your favorite fruits! Enjoy!")

else:
    print("You chose a new fruit. I hope you enjoy")


