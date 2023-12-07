# Initialize a 2d array

matrix = []
symbols = ['#', '*', '$', '-', '%', '+', '@', '&', '=', '/']


# Open file, build temp list with each char in a given line, append list to matrix
with open('input.txt') as file:
    for row in file:
        
        temp_list = []
        for char in row.strip():
            temp_list.append(char)

        matrix.append(temp_list)


def check_neighbor(i, j, boundaries_map):
    """Read in current value at index matrix[i][j]
    Calculate min and max values to avoid searching values outside of list
    If current value is numeric and adjacent to a symbol, return True
    """

    # If current_val not a number, return False
    if (matrix[i][j].isnumeric() == False):
        return False

    # Set min and max values
    row_min = boundaries_map['row_min']
    row_max = boundaries_map['row_max']
    col_min = boundaries_map['col_min']
    col_max = boundaries_map['col_max']


    # Search grid around current value for adjacent symbols
    for a in range(row_min, row_max + 1):
        for b in range(col_min, col_max + 1):
            if (a == i and b == j):
                continue
            else:
                if (matrix[a][b] in symbols):
                    print(f"Current val is {matrix[i][j]} and is adjacent to {matrix[a][b]}")
                    print(f"matrix[{i}][{j}] has adjac. symbol")
                    return True
                
    return False
    
# Set boundaries for search grid
def get_boundaries(i, j):
    """
    Evaluate upper and lower limits, set a min_row, max_row
    min_col, max_col where,
    rows correspond to outter-loop i values and 
    cols correspond to inner-loop j values
    """

    # Initialize hashmap to store boundary values
    boundaries = {}

    # Set min and max vals
    if ((i - 1) < 0):
        boundaries['row_min'] = i
    else:
        boundaries['row_min'] = i - 1
    
    if ((i + 1) > (len(matrix) - 1)):
        boundaries['row_max'] = i
    else:
        boundaries['row_max'] = i + 1

    if ((j - 1) < 0):
        boundaries['col_min'] = j
    else:
        boundaries['col_min'] = j - 1

    if ((j + 1) > (len(matrix[i]) - 1)):
        boundaries['col_max'] = j
    else:
        boundaries['col_max'] = j + 1

    return boundaries
    

# Search grid for each value in the matrix
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        is_neighbor = check_neighbor(i, j, get_boundaries(i, j))