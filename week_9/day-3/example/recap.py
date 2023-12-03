class Electronics:
    total_electronic = 0
    object_list = []

    # Tv should contain screen size
    # Laptop should contain ram size
    # Mobile should contain camera size

    def __init__(self, name, price, brand):
        self.name = name
        self.price = price
        self.brand = brand
        Electronics.total_electronic += 1

        # append object 
        Electronics.object_list.append(self)
        self.display()


    def __str__(self):
        return f"Name: {self.name}, Price: {self.price}, Brand: {self.brand}"
    
    def display(self):
        print(self)

    def save_json(self):
        # save a json representation of this object in ajson file
        file_name= "tv_json.json"
        with open(file_name, "w")as file:
            json.dump(self.__dict__, file)


    def load_json(self):
        # load a json and make my object resemble it
        # read the File 
        file_name= "tv_json.json"
        with open(file_name, "r")as file:
            
            json_dict = json.load(file)


            # make my object resemble it
          


    # Tv should contain screen size
    # Laptop should contain ram size
    # Mobile should contain camera size

class TV(Electronics):
    def __init__(self, name, price, brand, screen_size):
        self.screen_size = screen_size
        super().__init__(name, price, brand)
            
        def __str__(self):
            return f"Name: {self.name}, Price: {self.price}, Brand: {self.brand}, Screen Size: {self.screen_size}"
        
# laptop = Electronics("Laptop", 1000, "Dell")
television = Electronics("TV", 1000, "Samsung")
# mobile = Electronics("Mobile", 1000, "Apple")
# mouse = Electronics("Mouse", 50, "Logitech")
# call the json
television.save_json()

# run display
# laptop.display()


