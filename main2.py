import sys

def get_task_text(filepath):
    with open(filepath) as f:
        return f.read()
    
def formatting(text):
    result = []
        
    for string in text.splitlines():

        # the text is treated as one large, single-string file
        # the .splitlines() method separates it into individual strings by line
        
        stripped_string = string.strip()
        if not stripped_string: # if stripped_string is empty (False), we skip it
            continue   

        sanitized_dictionary = {"direction": '', "num": 0}
        sanitized_dictionary["direction"] = stripped_string[0]
        sanitized_dictionary["num"] = int(stripped_string[1:])
        result.append(sanitized_dictionary)
    
    return result
    
def calculation(list_of_dicts):
    initial_number = 50
    counter = 0
    sum_of_L = 0
    sum_of_R = 0

    for dictionary in list_of_dicts:
        if dictionary["direction"] == 'L':
            if dictionary["num"] < 100:
                new_number = initial_number - dictionary["num"]
                if (initial_number > 0 and new_number < 0) or (initial_number < 0 and new_number > 0):
                    counter += 1
                initial_number = new_number
                sum_of_L = sum_of_L + dictionary["num"]
            elif dictionary["num"] >= 100:
                normalized_number = (dictionary["num"] / 100)
                whole_part, fractional_part = divmod(normalized_number, 1)
                new_number = initial_number - fractional_part
                if (initial_number > 0 and new_number < 0) or (initial_number < 0 and new_number > 0):
                    counter += 1
                initial_number = new_number
                counter += whole_part
                sum_of_L = sum_of_L + dictionary["num"]
        elif dictionary["direction"] == 'R':
            if dictionary["num"] < 100:
                new_number = initial_number + dictionary["num"]
                if (initial_number > 0 and new_number < 0) or (initial_number < 0 and new_number > 0):
                    counter += 1
                initial_number = new_number
                sum_of_L = sum_of_L + dictionary["num"]
            elif dictionary["num"] >= 100:
                normalized_number = (dictionary["num"] / 100)
                whole_part, fractional_part = divmod(normalized_number, 1)
                new_number = initial_number + fractional_part
                if (initial_number > 0 and new_number < 0) or (initial_number < 0 and new_number > 0):
                    counter += 1
                initial_number = new_number
                counter += whole_part
                sum_of_L = sum_of_L + dictionary["num"]
        if (initial_number % 100) == 0: # every multiple of 100 is the dial "hitting" 0
                counter += 1
                print(f'Hit {counter} at direction {dictionary["direction"]} and number {dictionary["num"]}')
    
    print(f"sum_of_L is", sum_of_L)
    print(f"sum_of_R is", sum_of_R)
    return initial_number, counter
        
def main(filepath):
    text = get_task_text(filepath)
    formatted_text = formatting(text)
    print(calculation(formatted_text))

if len(sys.argv) == 2:
    filepath = sys.argv[1]
    main(filepath)
else:
    print("Usage: python3 main.py <path_to_file>")
    sys.exit(1)