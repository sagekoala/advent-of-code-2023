import math

# Read input into program

data = {}

with open('./input.txt', 'r') as file:
    for row in file:
        temp_split = row.strip().split(':')
        data[temp_split[0]] = list(map(int, temp_split[1].split()))

number_solutions = []

def get_number_solutions(time, distance):
    """Your toy boat has a starting speed of zero millimeters per millisecond. 
    For each whole millisecond you spend at the beginning of the race holding down the button, 
    the boat's speed increases by one millimeter per millisecond."""
    solutions = 0
    for i in range(time):
        remaining_time = time - i
        distance_traveled = remaining_time * i

        if (distance_traveled > distance):
            solutions+= 1

    number_solutions.append(solutions)


for i in range(len(data['Time'])):
    get_number_solutions(data['Time'][i], data['Distance'][i])
    
print(math.prod(number_solutions))