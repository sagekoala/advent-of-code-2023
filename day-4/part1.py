# Program to calculate score for winning scratch-off tickets
import collections

games_played = {}
scores = []

def populate_games_played(row):
        
        """Reads in row of input, splits row into game,
        winning_nums, current_nums and populates the
        games_played value with game num: [winning_nums, current_nums]"""

        split_line = row.strip().split(':')

        game = split_line[0].strip()
        split_games = split_line[1].split('|')

        winning_nums = split_games[0].strip().split()
        game_nums = split_games[1].strip().split()

        if (not game in games_played):
            games_played[game] = [winning_nums, game_nums]

def calculate_score():
     
     for key, value in games_played.items():

        print(key)

        winning_nums = value[0]
        game_nums = value[1]

        result = collections.Counter(winning_nums) & collections.Counter(game_nums)

        winning_amount = len(list(result.elements()))
        print(winning_amount)

        if (winning_amount != 0):

            count = 1
            for i in range(2, winning_amount + 1):
                count *= 2

            print(f"count amount {count}")

            scores.append(count)

     print(f"Total points = {sum(scores)}")
                
                
          



# Read in input:
with open('./input.txt') as file:
    for row in file:
        populate_games_played(row)

calculate_score()
        

    

    
