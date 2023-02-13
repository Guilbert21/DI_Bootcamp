class Animal:
    def __init__(self, name, count=1):
        self.name = name
        self.count = count

    def get_info(self):
        return f"{self.name}: {self.count}"

class Farm:
    def __init__(self, name):
        self.name = name
        self.animals = []

    def add_animal(self, name, count=1):
        new_animal = Animal(name, count)
        self.animals.append(new_animal)

    def get_info(self):
        info = []
        for animal in self.animals:
            info.append(animal.get_info())
        return "\n".join(info)

macdonald = Farm("McDonald")
macdonald.add_animal('cow',5)
macdonald.add_animal('sheep')
macdonald.add_animal('sheep')
macdonald.add_animal('goat', 12)
print(macdonald.get_info())



