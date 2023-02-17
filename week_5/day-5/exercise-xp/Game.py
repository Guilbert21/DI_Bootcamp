from random import randint

moves = ["rock", "paper", "scissor"]

class Player:
    def __init__(self,):
        self.choice = "None"
        self.score = 0

    def get_user_item(self, choice, run):
        z= 0
        for i in range(3):
            if choice == moves[i]:
                z = 1
        if z == 0:
            print("wrong")
            run = False
            return run
        if z == 1:
            print("Good")
            self.choice = choice
            return run
        
    def return_choice(self):
        return self.choice
    
    def check(self, computer, choice):
        if self.choice != "None":
            if self.choice == "rock" and get_computer_item == "scissor":
                self.score = self.score + 1
            elif self.choice == "rock" and get_computer_item == "paper":
                self.score = self.score - 1
            if self.choice == "paper" and get_computer_item == "rock":
                self.score = self.score + 1
            elif self.choice == "paper" and get_computer_item == "scissors":
                self.score = self.score - 1
            if self.score == "scissor" and get_computer_item == "paper":
                self.score = self.score + 1
            elif self.choice == "scissor" and get_computer_item == "rock":
                self.score = self.score - 1


    def return_score(self):
        return self.score
    
player = Player()
run = True
while run:
    run = player.get_user_item(input("Enter your choice:"),run)
    if run == True:
        get_computer_item = moves[randint(0,2)]
        print(f"the computer choice is {get_computer_item}")
        player.check(get_computer_item())
    print(player.return_score())
    