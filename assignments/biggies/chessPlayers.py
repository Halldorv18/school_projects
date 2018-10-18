def get_filename(prompt):
    filename = input(prompt)
    return filename

def create_key(name_of_player):
    last_name, first_name = name_of_player.split(",")
    full_name = first_name.strip() + " " + last_name.strip()
    return full_name

def process_value_data(chess_player_data):
    data_list = []
    data_list.append(int(chess_player_data[0].strip()))
    data_list.append(chess_player_data[2].strip())
    data_list.append(int(chess_player_data[3].strip()))
    data_list.append(int(chess_player_data[4].strip()))
    return data_list

def create_country_dict(name_values_dict):
    country_dict = {}
    for key, value in name_values_dict.items():
        country = value[1]
        if country in country_dict:
            country_dict[country].append(key)
        else:
            country_dict[country] = [key]
    return country_dict


def get_data_from_file(file_name):
    chess_player_dict = {} 
    try:
        with open(file_name, "r") as file_content:
            for line in file_content:
                line = line.split(";")
                key = create_key(line[1])
                player_data = process_value_data(line)
                chess_player_dict[key] = player_data
            
    except FileNotFoundError:
        pass
    return chess_player_dict

def print_header(string):
    print(string)
    print('-' * len(string))

def get_average_for_country(chess_player_dict, value):
    sum_of_elo = 0
    for player in value: 
        sum_of_elo += chess_player_dict[player][2]
    average = sum_of_elo / len(value)
    return average


def print_result(chess_player_dict, country_dict):
    for key, value in sorted(country_dict.items()):
        average = get_average_for_country(chess_player_dict, value)
        print("{} ({}) ({:.1f}):".format(key, len(value), average))
        for name in value:
            print("{:>40}{:>10d}".format(name, chess_player_dict[name][2]))


def main():       
    #1 get filename from user
    filename =  get_filename("Enter filename: ")
    #2 open the file
    chess_player_dict = get_data_from_file(filename)
    #3 process file data
    country_dict = create_country_dict(chess_player_dict)
    print_header("Players by country:")
    print_result(chess_player_dict, country_dict)






main()