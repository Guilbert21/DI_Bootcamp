class Dog():
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

    def bark(self):
        print(f"{self.name} is barking")

    def run_speed(self):
        speed = (self.weight/self.weight *10)
        print(f"{self.name} running speed is {speed}")

    def fight(self, other_dog):
        self_score = self.run_speed() * self.weight
        other_score = other_dog.run_speed() * other_dog.weight
        if self_score > other_score:
            return f"{self.name} won the fight"
        elif self_score < other_score:
            return f"{other_dog.name} won the fight"
        else:
            return "It was a tie"



dog1 = Dog("sam", 13, 25)
dog2 = Dog("rex", 3,20)
dog3 = Dog("tom", 5,30)
print(dog1.run_speed())

print(dog1.fight(dog3))  