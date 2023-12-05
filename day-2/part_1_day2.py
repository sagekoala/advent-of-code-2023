# Idea is to have a solution dict, key is going to be string Game #, value is going to be list of dicts from corresponding game
solution_dict = {}

# Initialize list of winning ids
winning_ids = []

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

def get_round_eligibility(round):
    """Read key value pairs for each round, compare against round limits for the 3 respective colors"""

    round_limits = {
        'red': 12,
        'green': 13,
        'blue': 14
    }
    
    for key, val in round.items():
        if (round[key] > round_limits[key]):
            return False
        
    return True

def manage_game(game, rounds):
    """Plays all rounds in a game, appends id to solution_nums if all rounds are eligible"""

    for round in rounds:
        if (get_round_eligibility(round) == False):
            print(f"{game} didn't pass")
            return False

    print(f"{game} passed all tests")
    manage_winning_ids(game)
    
    return True

def manage_winning_ids(game):
    """Reads in game string as parameter, appends integer value corresponding to game in winning_ids list"""

    winning_ids.append(int(parse_number(game)))

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
        manage_game(key, value)


print(f"The answer to part 1 is {sum(winning_ids)}")


