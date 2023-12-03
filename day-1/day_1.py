# Initialize empty list to store numbers that we parse from input.txt
numbers = []

def get_first_last_digits(text):
    """Reads string, returns first digit from left and first from right"""

    temp_solution = ""

    # Reading from the left
    for i in range(len(text)):
        if (text[i].isnumeric()):
            temp_solution += text[i]
            break

    # Reading from the right
    for i in range(len(text) - 1, -1, -1):
        if (text[i].isnumeric()):
            temp_solution += text[i]
            break

    return temp_solution

# Read input file
with open('./input.txt') as file:
    for row in file:
        numbers.append(int(get_first_last_digits(row)))


print(f"The solution is: {sum(numbers)}")