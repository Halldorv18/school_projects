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

def user_input():

size_of_game = int(input("Input dimension of the board:"))
board_list = make_list(size_of_game)

for line in board_list:

    print(line)
