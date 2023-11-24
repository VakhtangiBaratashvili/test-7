def welcome_and_rules() -> None:
    with open("welcome.txt", "r") as file:
        print(file.read())


def print_board(board: list) -> None:
    print(" _________________")
    print("|     |     |     |")
    print("|  " + board[0] + "  |  " + board[1] + "  |  " + board[2] + "  |")
    print("|_____|_____|_____|")
    print("|     |     |     |")
    print("|  " + board[3] + "  |  " + board[4] + "  |  " + board[5] + "  |")
    print("|_____|_____|_____|")
    print("|     |     |     |")
    print("|  " + board[6] + "  |  " + board[7] + "  |  " + board[8] + "  |")
    print("|_____|_____|_____|")


def check_win(board: list, blank: str) -> bool:
    winning_combos: list = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    for winning_combo in winning_combos:
        if board[winning_combo[0]] == board[winning_combo[1]] == board[winning_combo[2]] and board[
            winning_combo[0]] != blank:
            return True
    return False


def check_tie(board: list, blank: str) -> bool:
    return blank not in board


def player_turn(player: str) -> str:
    return "O" if player == "X" else "X"


def result(file: str) -> None:
    with open(file, "r") as file:
        print(file.read())


def tic_tac_toe() -> None:
    blank_space: str = " "
    play_board: list = [blank_space] * 9
    current_player: str = "X"
    print_board(play_board)
    while True:
        try:
            position: int = int(input(f"Enter Position for {current_player}: "))
            while position < 1 or position > 9 or play_board[position - 1] != blank_space:
                print("invalid input, try again")
                position = int(input(f"Enter Position for {current_player}: "))
            play_board[position - 1] = current_player
            print_board(play_board)
            if check_win(play_board, blank_space):
                file_name: str = f"{current_player.lower()}_wins.txt"
                result(file_name)
                break
            elif check_tie(play_board, blank_space):
                file_name: str = f"tie.txt"
                result(file_name)
                break
            else:
                current_player = player_turn(current_player)

        except ValueError:
            print("Invalid input, Enter number")


def play_again() -> None:
    while True:
        choice: str = input("Do you want to play again(yes/no): ")
        while choice.lower() != "yes" and choice.lower() != "no":
            choice = input("Enter yes or no: ")
        if choice.lower() == "yes":
            tic_tac_toe()
        else:
            print("Game Ended")
            break


if __name__ == "__main__":
    welcome_and_rules()
    tic_tac_toe()
    play_again()
