class Dog:
    def __init__(self, name, height):
        self.name = name
        self.height = height
        
    def bark(self):
        print(f"{self.name} goes woof!")
        
    def jump(self):
        print(f"{self.name} jumps {self.height * 2} cm high!")

davids_dog = Dog("Rex", 50)
print("Details of David's dog:")
print(f"Name: {davids_dog.name}")
print(f"Height: {davids_dog.height} cm")
davids_dog.bark()
davids_dog.jump()

sarahs_dog = Dog("Teacup", 20)
print("\nDetails of Sarah's dog:")
print(f"Name: {sarahs_dog.name}")
print(f"Height: {sarahs_dog.height} cm")
sarahs_dog.bark()
sarahs_dog.jump()

if davids_dog.height > sarahs_dog.height:
    print(f"\n{davids_dog.name} is bigger.")
else:
    print(f"\n{sarahs_dog.name} is bigger.")
