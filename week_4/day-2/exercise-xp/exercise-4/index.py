decimal = [1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5]
other = int(input("Enter how many other sequence you want:"))

for i in range(other):
    add = (decimal[-1] + 0.5)
    decimal.append(add)

print(decimal)