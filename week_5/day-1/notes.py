# # # class Dog():
# # #     def __init__(self):
# # #         pass
# # #     pass

# # # class Human():
# # #     pass

# # # class Pizza():
# # #     pass

# # # # my_dog = Dog()

# # # class Tower():
# # #     def __init__(self):
# # #       print("Creating tower..")

# # # cybercity = Tower()

class Car():
    def __init__(self, brand, color):
        print("Creation car...")
        self.brand = brand
        self.color = color
        self.engine_started = False

    def start_engine(self):
        self.engine_started = True

    def stop_engine(self):
        self.engine_started = False

    def accelerate(self):
        if self.engine_started:
            print("Accelerating to the speed of sound...")

        else:
            print("start the engine first")

    def display_info(self):
        print(f"my {self.brand} is {self.color}")

    
my_car = Car("Toyota", "Red")
my_car.start_engine()
my_car.accelerate()
my_car.stop_engine()
my_car.accelerate()
my_car.display_info()
    

# # my_garage = []


# class Button():
#     def __init__(self, color, text):
#         self.color = color
#         self.text = text

#     def 

class BankAccount:

    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance
        self.transactions = []

    def view_balance(self):
        self.transactions.append("View Balance")
        print(f"Balance for account {self.account_number}: {self.balance}")

    def deposit(self, amount):
        if amount <= 0:
            print("Invalid amount")
        elif amount < 100:
            print("Minimum deposit is 100")
        else:
            self.balance += amount
            self.transactions.append(f"Deposit: {amount}")
            print("Deposit Succcessful")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient Funds")
        else:
            self.balance -= amount
            self.transactions.append(f"Withdraw: {amount}")
            print("Withdraw Approved")
            return amount

    def view_transactions(self):
        print("Transactions:")
        print("-------------")
        for transaction in self.transactions:
            print(transaction)
