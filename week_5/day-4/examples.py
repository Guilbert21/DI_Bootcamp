from faker import Faker
fake = Faker()

with open ("output.txt", "w") as f:
    for i in range(1000):
        f.write(f"{fake.email()}\n")
        
for line in open("output.txt"):
    print(line)