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

    def winner(self, letter, square):
        # Check if there is a three-in-a-row in the row
        row_index = square // 3
        if all(self.board[row_index * 3 + i] == letter for i in range(3)):
            print(f"{letter} player wins!")
            return True

        # Check if there is a three-in-a-row in the column
        col_index = square % 3
        if all(self.board[col_index + 3 * i] == letter for i in range(3)):
            print(f"{letter} player wins!")
            return True

        # Check if there is a three-in-a-row in the main diagonal
        if all(self.board[i] == letter for i in [0, 4, 8]):
            print(f"{letter} player wins!")
            return True

        # Check if there is a three-in-a-row in the anti-diagonal
        if all(self.board[i] == letter for i in [2, 4, 6]):
            print(f"{letter} player wins!")
            return True

        return False


    def make_move(self, letter, square):
        self.board[square] = letter
        self.print_board()

        

def TicTacToe():
    x_player = HumanPlayer("X")
    o_player = RandomComputerPlayer("O")
    game = Game()
    next_move = "X"
    Game.print_board_numbers()
    print("------------")

    while game.empty_squares():

        if next_move == "X":
            print("It's X's turn.")
            square = x_player.get_move(game)
            game.make_move("X", square)
            
            if game.winner("X", square):
                break
            else:
                next_move = "O"

        if next_move == "O":
            print("It's O's turn.")
            square = x_player.get_move(game)
            game.make_move("O", square)
            
            if game.winner("O", square):
                break
            else:
                next_move = "X"
        

    if not game.empty_squares():
        print("It's a tie!")

if __name__ == "__main__":
    TicTacToe()



    
