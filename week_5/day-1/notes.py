# # # # # # # # # # class Dog():
# # # # # # # # # #     def __init__(self):
# # # # # # # # # #         pass
# # # # # # # # # #     pass

# # # # # # # # # # class Human():
# # # # # # # # # #     pass

# # # # # # # # # # class Pizza():
# # # # # # # # # #     pass

# # # # # # # # # # # my_dog = Dog()

# # # # # # # # # # class Tower():
# # # # # # # # # #     def __init__(self):
# # # # # # # # # #       print("Creating tower..")

# # # # # # # # # # cybercity = Tower()

# # # # # # # class Car():
# # # # # # #     def __init__(self, brand, color):
# # # # # # #         print("Creation car...")
# # # # # # #         self.brand = brand
# # # # # # #         self.color = color
# # # # # # #         self.engine_started = False

# # # # # # #     def start_engine(self):
# # # # # # #         self.engine_started = True

# # # # # # #     def stop_engine(self):
# # # # # # #         self.engine_started = False

# # # # # # #     def accelerate(self):
# # # # # # #         if self.engine_started:
# # # # # # #             print("Accelerating to the speed of sound...")

# # # # # # #         else:
# # # # # # #             print("start the engine first")

# # # # # # #     def display_info(self):
# # # # # # #         print(f"my {self.brand} is {self.color}")

    
# # # # # # # my_car = Car("Toyota", "Red")
# # # # # # # my_car.start_engine()
# # # # # # # my_car.accelerate()
# # # # # # # my_car.stop_engine()
# # # # # # # my_car.accelerate()
# # # # # # # my_car.display_info()
    

# # # # # # # # # my_garage = []


# # # # # # # # class Button():
# # # # # # # #     def __init__(self, color, text):
# # # # # # # #         self.color = color
# # # # # # # #         self.text = text

# # # # # # # #     def 

# # # # # # # class BankAccount:

# # # # # # #     def __init__(self, account_number, balance=0):
# # # # # # #         self.account_number = account_number
# # # # # # #         self.balance = balance
# # # # # # #         self.transactions = []

# # # # # # #     def view_balance(self):
# # # # # # #         self.transactions.append("View Balance")
# # # # # # #         print(f"Balance for account {self.account_number}: {self.balance}")

# # # # # # #     def deposit(self, amount):
# # # # # # #         if amount <= 0:
# # # # # # #             print("Invalid amount")
# # # # # # #         elif amount < 100:
# # # # # # #             print("Minimum deposit is 100")
# # # # # # #         else:
# # # # # # #             self.balance += amount
# # # # # # #             self.transactions.append(f"Deposit: {amount}")
# # # # # # #             print("Deposit Succcessful")

# # # # # # #     def withdraw(self, amount):
# # # # # # #         if amount > self.balance:
# # # # # # #             print("Insufficient Funds")
# # # # # # #         else:
# # # # # # #             self.balance -= amount
# # # # # # #             self.transactions.append(f"Withdraw: {amount}")
# # # # # # #             print("Withdraw Approved")
# # # # # # #             return amount

# # # # # # #     def view_transactions(self):
# # # # # # #         print("Transactions:")
# # # # # # #         print("-------------")
# # # # # # #         for transaction in self.transactions:
# # # # # # #             print(transaction)


# # # # # class PlayerCharacter:
# # # # #     membership = True
# # # # #     def __init__(self, name, age):
# # # # #         if (self.membership):
# # # # #          self.name = name
# # # # #          self.age = age

# # # # #     def  shout(self):
# # # # #         print(f"my name is {self.name}")
# # # # #         # return "done"

# # # # #     def  run(self, hello):
# # # # #         print(f"my name is {self.name}")
    
# # # # # player1 = PlayerCharacter("Alexis", 10)
# # # # # player2 = PlayerCharacter("Tom", 21)
# # # # # player2.attack = 50

# # # # # # # print(player1.run("hello"))
# # # # # # # print(player2.membership)


# # # # # #       #inheritance
# # # # # # class User:
# # # # # #     def sign_in(self):
# # # # # #         print("logged in")

# # # # # # class Wizard(User):
# # # # # #     def __init__(self,name, power):
# # # # # #         self.name = name
# # # # # #         self.power = power

# # # # # #     def attack(self):
# # # # # #         print(f"attacking with power of {self.power}")

# # # # # # class Archer(User):
# # # # # #      def __init__(self,name, num_arrows):
# # # # # #         self.name = name
# # # # # #         self.num_arrows = num_arrows

# # # # # #      def attack(self):
# # # # # #         print(f"attacking with arrows : arrows left {self.num_arrows}")

# # # # # # wizard1 = Wizard("Merlin", 50)
# # # # # # archer1 = Archer("Robin", 100) 
# # # # # # wizard1.attack()
# # # # # # archer1.attack()

# # # # # class MyClass(object):
# # # # #     def func(self):
# # # # #         print("I'm being called from the Parent class")




# # # # # class ChildClass(MyClass):
# # # # #     def func(self):
# # # # #         print("I'm actually being called from the Child class")
# # # # #         print("But...")
# # # # #         # Calling the `func()` method from the Parent class.
# # # # #         super(ChildClass, self).func()

# # # # # my_instance_2 = ChildClass()
# # # # # my_instance_2.func()


# # # # # class Parrot():

# # # # #     def fly(self):
# # # # #         print("Parrot can fly")

# # # # #     def swim(self):
# # # # #         print("Parrot can't swim")

# # # # # class Penguin():

# # # # #     def fly(self):
# # # # #         print("Penguin can't fly")

# # # # #     def swim(self):
# # # # #         print("Penguin can swim")

# # # # # # common interface
# # # # # def flying_test(bird):
# # # # #     bird.fly()

# # # # # def swim_test(penguin):
# # # # #     penguin.swim()

# # # # # #instantiate objects
# # # # # blu = Parrot()
# # # # # peggy = Penguin()

# # # # # # passing the object
# # # # # flying_test(blu)
# # # # # # >> Parrot can fly

# # # # # flying_test(peggy)
# # # # # # >> Penguin can't fly

# # # # # swim_test(blu)


# # # # # attributes

# # # # # class Dog():
# # # # #     dogs_king = "Bernie IV"

# # # # #     # Initializer / Instance Attributes
# # # # #     def __init__(self, name_of_the_dog):
# # # # #         print("A new dog has been initialized !")
# # # # #         print("His name is", name_of_the_dog)
# # # # #         self.name = name_of_the_dog

# # # # #     def bark(self):
# # # # #         print("{} barks ! WAF".format(self.name))

# # # # #     def walk(self, number_of_meters):
# # # # #         print("{} walked {} meters".format(self.name, number_of_meters))

# # # # #     def rename(self, new_name):
# # # # #         self.name = new_name

# # # # # my_dog = Dog("Rex")
# # # # # my_dog.rename("Paul")


# # # # class Circle:
# # # #     color = "red"

# # # #     def __init__(self, diameter):
# # # #         self.diameter = diameter

# # # #     def grow(self, factor=2):
# # # #         self.diameter = self.diameter * factor

# # # #     def get_color(self):
# # # #        return Circle.color

# # # # circle1 = Circle(2)
# # # # print(circle1.color)
# # # # print(Circle.color)
# # # # print(circle1.get_color())
# # # # circle1.grow(3)
# # # # print(circle1.diameter)


# # # class MyClass(object):
# # #     count = 0

# # #     def __init__(self, val):
# # #         self.val = val
# # #         MyClass.count += 1

# # #     def set_val(self, newval):
# # #         self.val = newval

# # #     def get_val(self):
# # #         return self.val

# # #     @classmethod
# # #     def get_count(cls):
# # #         return cls.count

# # # object_1 = MyClass(10)
# # # print("\nValue of object : %s" % object_1.get_val())
# # # print(MyClass.get_count())

# # # object_2 = MyClass(20)
# # # print("\nValue of object : %s" % object_2.get_val())
# # # print(MyClass.get_count())


# class MyClass(object):
#     count = 0

#     def __init__(self, val):
#         self.val = self.filterint(val)
#         MyClass.count += 1

#     @staticmethod
#     def filterint(value):
#         if not isinstance(value, int):
#             print("Entered value is not an INT, value set to 0")
#             return 0
#         else:
#             return value


# a = MyClass("5")
# b = MyClass(10)
# c = MyClass(15)

# print(a.val)
# print(b.val)
# print(c.val)
# print(a.filterint(100))

class PrintList(object):

    def __init__(self, my_list):
        self.mylist = my_list

    def __repr__(self):
        return str(self.mylist)


printlist = PrintList(["a", "b", "c"])
print(printlist.__repr__())

