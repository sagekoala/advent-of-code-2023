# Program to solve number of solutions given a time and a distance

data = {}

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

    return solutions

with open('./input.txt', 'r') as file:

    # Strip text, parse into field and num and store it
    for row in file:
        tmp_split = row.strip().split()
        
        field = tmp_split[0]
        num = int(''.join(tmp_split[1::]))

        data[field] = num

print(f"Solution is {get_number_solutions(data['Time:'], data['Distance:'])} different ways.")