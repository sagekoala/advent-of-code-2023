from itertools import islice

clean_data = []

data = []

maps = []

seed_to_soil = {}

final_values = {}

# Program to map seed numbers to location numbers
with open('./example_input.txt') as file:

    seeds = ''.join(islice(file, 0, 1)).strip().split(': ')
    for row in file:
        if (row[0] != "\n"):
            clean_data.append(row.strip())
    

    temp_list = []
    for line in clean_data:
        if (line[0].isnumeric() is False and temp_list):
            data.append(temp_list)
            temp_list = []
            data.append(line.strip())
        elif (line[0].isnumeric() is False and not temp_list):
            data.append(line.strip())
        else:
            temp_val = line.strip()
            temp_list.append(list(map(int, line.split())))

    # Apend final list of numbers
    data.append(temp_list)


for i in range(0, len(data) - 1, 2):
    temp_dict = {data[i]: data[i + 1]}
    maps.append(temp_dict)

# Printing data
print(seeds)
for dict in maps:
    for key, val in dict.items():
        print(f"{key} {val}")

def map_source_to_destination(two_d_list):

    temp_dict = {}

    # Add source to destination based on map
    for item in two_d_list:
        for i in range(item[1], item[1] + item[2]):
            temp_dict[i] = item[0] + (i - item[1]) 

    for i in range(100):
        if (i not in temp_dict):
            temp_dict[i] = i

    return temp_dict

keys = maps[0]['seed-to-soil map:']
print(sorted(map_source_to_destination(keys).items()))



