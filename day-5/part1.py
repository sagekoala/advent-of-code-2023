# Program to map seed numbers to location numbers
from itertools import islice

clean_data = []

data = []

# List of dicts
maps = []

seed_to_soil = {}

list_of_mapped_values = []

def map_source_to_destination(map_name, two_d_list):

    temp_dict = {}

    # Add source to destination based on map
    for item in two_d_list:
        for i in range(item[1], item[1] + item[2]):
            temp_dict[i] = item[0] + (i - item[1]) 

    for i in range(100):
        if (i not in temp_dict):
            temp_dict[i] = i

    return {map_name: temp_dict}


with open('./example_input.txt') as file:

    # Store seed numbers
    seeds = ''.join(islice(file, 0, 1)).strip().split(': ')

    # Filter empty rows
    for row in file:
        if (row[0] != "\n"):
            clean_data.append(row.strip())
    
    # Populate data with text as string elements, numbers as list of lists
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

# Mapping source to destination for each dict in maps list
print(seeds)
for dict in maps:
    for key, val in dict.items():
        list_of_mapped_values.append(map_source_to_destination(key, val))

for list_item in list_of_mapped_values:
    print(list_item)

"""for key, val in maps[0].items():
    print(sorted(map_source_to_destination(key, val).items(), key=lambda item: item[1]))
"""


