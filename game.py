from player import HumanPlayer, RandomComputerPlayer

class Game:
    def __init__(self):
        self.board = [" " for _ in range(9)]
        self.current_winner = None

    def print_board(self):
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print("| " + " | ".join(row) + " |")

    @staticmethod
    def print_board_numbers():
        number_board = [ str(_) for _ in range(9)]
        for row in [number_board[i*3:(i+1)*3] for i in range(3)]:
            print("| " + " | ".join(row) + " |")

    def available_moves(self):
        return [i for i, spot in enumerate(self.board) if spot == " "]
    
    def empty_squares(self):
        return " " in self.board

    def winner(self, square, letter):

        #checking if there is a three-in-a-row in the row
        row_index = square // 3
        #This code is to check if all the elements in a row are same or not.
        #And for that, built in function, all() has been used.
        #If all three elements of the row are same, a winner message will be printed
        #and the method will return True
        if all([self.board[row_index * 3 : (row_index + 1) *3]]):
            print(f"{letter} player wins!")
            return True

        #Checking if there is a three-in-a-row in the column
        col_index = square % 3
        #Not really sure if this code will work. Will get back to this
        if all([self.board[i] for i in self.board.count if i % 3 == col_index]):
            print(f"{letter} player wins!")
            return True
        
        #Checking if there is a three-in-a-row in any diagonal line
        
        #This will check if there is any three-in-a-row in any of the two diagonals
        #The two diagonals are [0,4,8] and [2,4,6]
        if all([self.board[i] for i in [0,4,8]]):
            print(f"{letter} player wins!")
            return True
        
        if all([self.board[i] for i in [2,4,6]]):
            print(f"{letter} player wins!")
            return True



        

def TicTacToe():
    x_player = HumanPlayer("X")
    o_player = RandomComputerPlayer("O")

    next_move = "X"
    
    #Not sure if this code will work because I haven't created a object of the Game class.
    while Game.winner():
        Game.print_board_numbers()


    


