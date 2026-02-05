def print_board(board):
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")

def board_guide():
    print("Board positions:")
    print(" 1 | 2 | 3 ")
    print("---+---+---")
    print(" 4 | 5 | 6 ")
    print("---+---+---")
    print(" 7 | 8 | 9 ")

def choose_player():
    print("Choose your player: X or O")
    player = input().upper()
    if player not in ['X', 'O']:
        print("Invalid choice. Please choose X or O.")
        return choose_player()
    return player

def switch_player(player):
    if player == 'X':
        return 'O'
    else:
        return 'X'
    
def check_winner(board):
    winning_combinations = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8), 
        (0, 3, 6), (1, 4, 7), (2, 5, 8), 
        (0, 4, 8), (2, 4, 6)  
    ]
    tie_combo = ---
    for combo in winning_combinations:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] != ' ':
            return board[combo[0]]

    for 
    return None

def get_valid_move(player, board):
    while True:
        try:
            move = input(f"Player {player}, enter your move (1-9): ")
            if not move.isdigit():
                print("Invalid move. Please enter a number between 1 and 9.")
            elif board[int(move) - 1] != ' ':
                print("That position is already taken. Please choose another.")
            else:
                return int(move) - 1
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 9.")

def main():
    print("Welcome to a new round of Tic-Tac-Toe!")
    max_moves = 9
    current_move = 0
    player = choose_player()
    board_guide()
    board = [' ' for _ in range(9)]

    while current_move < max_moves:
        move = get_valid_move(player, board)
        board[move] = player
        current_move = current_move + 1
        print_board(board)
        winner = check_winner(board)
        if winner:
            print(f"Player {winner} wins!")
            return
        player = switch_player(player)

# Tic-tac-toe game
if __name__ == "__main__":
    main()
