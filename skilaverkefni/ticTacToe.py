def make_list(size):
    return_list = []
    last_number = 0
    for size_range in range(1, size + 1):
        THE_LIST = []
        for number in range(last_number + 1, last_number + size + 1):
            THE_LIST.append(number)
        last_number = number
        return_list.append(THE_LIST)
    return return_list

def user_input(next_move):
    while True:
        if next_move == "X":
            user_choice = int(input("X position: "))
            break
        elif next_move == "O":
            user_choice = int(input("O position: "))
            break
        else:
            print("Illegal move!")
            continue
    return user_choice
    
    
def change_board(user_choice, x_or_o, board_list):
    for lines in board_list:
        for index, positions in enumerate(lines):
            if user_choice == positions:
                lines.remove(positions)
                lines.insert(index, x_or_o)
    return board_list

def print_board(board_list):
    for lines in board_list:
        for position in lines:
            print("{:5}".format(position)) # er ekki ad na ad prenta í linu...
victory = False
next_move = "X"
while not victory:
    size_of_game = int(input("Input dimension of the board:"))
    board_list = make_list(size_of_game)
    print_board(board_list)
    user_choice = user_input(next_move)
    board_list = change_board(user_choice, next_move, board_list)
    print_board
    print(board_list)
    if next_move == "X":
        next_move = "O"
    elif next_move == "O":
        next_move = "X"



