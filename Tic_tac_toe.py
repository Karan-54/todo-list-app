# Tic Tac Toe Game in Python

# Initialize the board (3x3 grid)
board = [' ' for _ in range(9)]

def print_board():
    print("\n")
    print(" {} | {} | {} ".format(board[0], board[1], board[2]))
    print("---+---+---")
    print(" {} | {} | {} ".format(board[3], board[4], board[5]))
    print("---+---+---")
    print(" {} | {} | {} ".format(board[6], board[7], board[8]))
    print("\n")

def check_win():
    win_conditions = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),  # Rows
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Columns
        (0, 4, 8), (2, 4, 6)              # Diagonals
    ]
    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] != ' ':
            return board[condition[0]]
    if ' ' not in board:
        return 'Tie'
    return False

def is_valid_move(move):
    return move.isdigit() and 1 <= int(move) <= 9 and board[int(move) - 1] == ' '

def main():
    while True:
        global board
        board = [' ' for _ in range(9)]  # Reset the board
        current_player = 'X'
        
        while True:
            print_board()
            move = input(f"Player {current_player}, enter your move (1-9): ")

            if not is_valid_move(move):
                print("⚠️ Invalid move! Please enter a number between 1-9 that is not already taken.")
                continue
            
            move = int(move) - 1
            board[move] = current_player

            result = check_win()
            if result:
                print_board()
                if result == 'Tie':
                    print("😲 It's a tie!")
                else:
                    print(f"🎉 Player {result} wins! 🎉")
                break

            current_player = 'O' if current_player == 'X' else 'X'

        # Ask for replay
        replay = input("🔁 Do you want to play again? (yes/no): ").strip().lower()
        if replay != 'yes':
            print("Thanks for playing! 🎮")
            break

if __name__ == '__main__':
    main()
