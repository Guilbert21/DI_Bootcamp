number = int(input("Enter a number: "))
length = int(input("Enter a length: "))

list = []

for i in range(0, length):
    # temp = int(input("enter a number"))
    temp = number * (i + 1)
    list.append(temp)
print(list)


