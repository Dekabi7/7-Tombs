class TicTacToe:
    def __init__(self):
        # Initialize empty 3x3 board
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        self.current_player = 'X'
    
    def display_board(self):
        """Display the current state of the board"""
        print("\n   0   1   2")
        for i in range(3):
            print(f"{i}  {self.board[i][0]} | {self.board[i][1]} | {self.board[i][2]}")
            if i < 2:
                print("  -----------")
        print()
    
    def make_move(self, row, col):
        """Make a move on the board if the position is valid and empty"""
        if 0 <= row < 3 and 0 <= col < 3 and self.board[row][col] == ' ':
            self.board[row][col] = self.current_player
            return True
        return False
    
    def check_winner(self):
        """Check if there's a winner"""
        # Check rows
        for row in self.board:
            if row[0] == row[1] == row[2] != ' ':
                return row[0]
        
        # Check columns
        for col in range(3):
            if self.board[0][col] == self.board[1][col] == self.board[2][col] != ' ':
                return self.board[0][col]
        
        # Check diagonals
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != ' ':
            return self.board[0][0]
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != ' ':
            return self.board[0][2]
        
        return None
    
    def is_board_full(self):
        """Check if the board is full (tie game)"""
        for row in self.board:
            if ' ' in row:
                return False
        return True
    
    def switch_player(self):
        """Switch between X and O players"""
        self.current_player = 'O' if self.current_player == 'X' else 'X'
    
    def reset_board(self):
        """Reset the board for a new game"""
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        self.current_player = 'X'


def main():
    """Main game loop"""
    game = TicTacToe()
    
    print("Welcome to Tic-Tac-Toe!")
    print("Players will take turns. Player X goes first.")
    print("Enter row and column numbers (0-2) to make your move.")
    
    while True:
        game.display_board()
        
        # Get player input
        try:
            print(f"Player {game.current_player}'s turn")
            row = int(input("Enter row (0-2): "))
            col = int(input("Enter column (0-2): "))
            
            # Make the move
            if game.make_move(row, col):
                # Check for winner
                winner = game.check_winner()
                if winner:
                    game.display_board()
                    print(f"🎉 Player {winner} wins!")
                    break
                
                # Check for tie
                if game.is_board_full():
                    game.display_board()
                    print("It's a tie! 🤝")
                    break
                
                # Switch to next player
                game.switch_player()
            else:
                print("❌ Invalid move! That position is already taken or out of bounds.")
        
        except (ValueError, IndexError):
            print("❌ Invalid input! Please enter numbers between 0 and 2.")
        except KeyboardInterrupt:
            print("\n\nThanks for playing!")
            break
    
    # Ask if they want to play again
    while True:
        try:
            play_again = input("\nWould you like to play again? (y/n): ").lower().strip()
            if play_again in ['y', 'yes']:
                game.reset_board()
                main()
                break
            elif play_again in ['n', 'no']:
                print("Thanks for playing Tic-Tac-Toe! 👋")
                break
            else:
                print("Please enter 'y' for yes or 'n' for no.")
        except KeyboardInterrupt:
            print("\n\nThanks for playing!")
            break


if __name__ == "__main__":
    main()