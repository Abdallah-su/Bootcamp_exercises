import random

class Game:
    def __init__(self):
       pass
    def get_user_item(self):
        while True:
            user_item = input("select from the options(R=rock/P=paper/S=scissors or Q to quit: ")
            if user_item == "R":
                return "Rock"
            elif user_item == "P":
                return "Paper"
            elif user_item == "S":
                return "Scissors"
            else:
                return ValueError("invalid input, choose from the options above")  
                     
    def get_computer_item(self):
        options = ["Rock", "Paper", "Scissors"]
        computer_item = random.choice(options)
        return computer_item
    
    def get_game_result(self, user_item, computer_item):
        if user_item == computer_item:
            return  "tie"
        elif user_item == "Rock" and computer_item == "Scissors":
            return  "win"
        elif user_item == "Paper" and computer_item ==  "Rock" :
             return  "win"
        elif user_item == "Scissors" and computer_item == "Paper":
             return  "win"
        else:
            return  "loss"


    def play(self):
        while True:
            user= self.get_user_item()
            computer= self.get_computer_item()
            results = self.get_game_result(user, computer)
            print(f"you selected {user} and the computer chose {computer},{results}")
            results