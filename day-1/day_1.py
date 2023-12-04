# Initialize empty lists to store numbers that parsed from input.txt
nums = []

written_nums = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

def number_in_text_left(text):
    """Reads string, returns first digit or written number from left and first from right"""
    temp_answer = ""

    # Reading each char from left, building substring, breaking if digit or numerical
    # word is found
    temp_str = ""
    for char in text:
        if (char.isnumeric()):
            temp_answer += char
            break
        else:
            temp_str += char
            if (temp_str in written_nums):
                temp_answer += str((written_nums.index(temp_str) + 1))
                break
            elif (get_all_substrings(temp_str)):
                temp_answer += str((get_all_substrings(temp_str)))
                break
    

    return temp_answer

def number_in_text_right(text):
    """Reads the digit from the right"""
    temp_answer = ""

    temp_str = ""
    for char in reversed(text):
        if (char.isnumeric()):
            temp_answer += char
            break
        else:
            temp_str += char
            if (temp_str[::-1] in written_nums):
                temp_answer += str(((written_nums.index(temp_str[::-1]) + 1)))
                break
            elif (get_all_substrings(temp_str[::-1])):
                temp_answer += str(get_all_substrings(temp_str[::-1]))
                break

    return temp_answer

def get_all_substrings(text):
    """Build list of all possible substrings, return index if substring in written_num list"""

    substr_list = []

    for i in range(len(text)):
        for j in range(i+1, len(text) + 1):
            substr_list.append(text[i:j])

    for item in substr_list:
        if item in written_nums:
            return (written_nums.index(item) + 1)
        
    return 0

def append_numbers_to_list(text):
    """Reads string, returns first digit or written number from left and first from right"""

    temp_answer = number_in_text_left(text) + number_in_text_right(text)
    nums.append(int(temp_answer))

# Read input file
with open('./input.txt') as file:
    for row in file:
        append_numbers_to_list(row)
        

print(f"The solution is: {sum(nums)}")
