class Zoo:
    def __init__(self, zoo_name):
        self.name = zoo_name
        self.animals = []

    def add_animal(self, new_animal):
        if new_animal not in self.animals:
            self.animals.append(new_animal)
        else:
            print(f"{new_animal} is already in the zoo.")

    def get_animals(self):
        print("Animals in the zoo:")
        for animal in self.animals:
            print(animal)

    def sell_animal(self, animal_sold):
        if animal_sold in self.animals:
            self.animals.remove(animal_sold)
            print(f"{animal_sold} has been sold.")
        else:
            print(f"{animal_sold} is not in the zoo.")

    def sort_animals(self):
        animal_dict = {}
        for animal in self.animals:
            first_letter = animal[0]
            if first_letter not in animal_dict:
                animal_dict[first_letter] = [animal]
            else:
                animal_dict[first_letter].append(animal)
        for key in sorted(animal_dict.keys()):
            print(key.upper() + ":")
            for animal in sorted(animal_dict[key]):
                print("   " + animal)

