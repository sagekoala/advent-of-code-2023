import numpy as np

# Idea is to have a solution dict, key is going to be string Game #, value is going to be list of dicts from corresponding game
solution_dict = {}

# Initialize list of winning ids
min_round_dicts = []

powers = []

def build_dict(text):
    temp_list = text.split(', ')

    current_dict = {}

    # Split value from key
    for item in temp_list:
        color = parse_color(item)

        if (not color in current_dict):
            current_dict[color] = int(parse_number(item))

    return current_dict

def parse_color(text):
    color = ""

    for i in range(len(text) - 1, -1, -1):
        if (text[i] != " "):
            color += text[i]
        else:
            return color[::-1]
        
def parse_number(text):
    num = ""
    for char in text:
        if (char.isnumeric()):
            num += char

    return num
        
def build_list_of_dicts(text):
    """Builds list of dicts to serve as value for key:value pair in solutions dict"""

    list_of_dicts = []

    rounds = text.split(";")

    for round in rounds:
        list_of_dicts.append(build_dict(round.lstrip()))

    return list_of_dicts

def get_minimum_round(round):
    """Read key value pairs for each round, compare against round limits for the 3 respective colors"""

    minimum_round = {}
    
    for key, val in round.items():
        if (not key in minimum_round):
            minimum_round[key] = val
        elif (round[key] > minimum_round[key]):
            minimum_round[key] = val

    return minimum_round
    
        
def manage_game(rounds):
    """Plays each round in a game, appends appends dict representing minimum possible round to min_round_dicts list"""

    current_min_round = {}

    for round in rounds:
        min_to_evaluate = get_minimum_round(round)
        
        for key, value in min_to_evaluate.items():
            if (key not in current_min_round):
                current_min_round[key] = value
            elif (min_to_evaluate[key] > current_min_round[key]):
                current_min_round[key] = value

    min_round_dicts.append(current_min_round) 

def get_powers():
    """A power is the product of the minimum possible value for red, green, and blue respectively in a single complete series of rounds"""

    temp_list = []

    for dict in min_round_dicts:
        for key, value in dict.items():
            temp_list.append(value)

        powers.append(np.prod(temp_list))
        temp_list = []

# Read input
with open('./input.txt') as file:
    for row in file:
        split_row = row.split(": ")

        # Parse input, populate solution dict
        # Going to be key for key:value pair in 
        game_number = split_row[0]

        # Pass first argument of split_row with strip() method to remove new line character
        list_of_dicts = build_list_of_dicts(split_row[1].strip())

        solution_dict[game_number] = list_of_dicts
        
    for key, value in solution_dict.items():
        manage_game(value)

    get_powers()

    print(f"The solution to part 2 is {sum(powers)}")