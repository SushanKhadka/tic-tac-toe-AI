import random

class Player:
    def __init__(self, letter):
        self.letter = letter

class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        #We have a value boolean which will be true if the user entered move is available. 
        #We are using an if statement inside a while loop that checks if the input is valid or not,
        #and the while loop will run until the value is valid.
        value = False
        val = int(input("Enter a number between (0,8)"))

        while value:
            if(val not in game.available_moves()):
                print("Invalid input, please try again")
                val = int(input("Enter a number between (0,8)"))
            else:
                value = True

        

class RandomComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        return random.choice(game.available_moves())