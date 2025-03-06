import re

def process_string(input_string):
    if input_string == "":
        return 0

def process_number(input_number):
    return input_number

def process_two_numbers_comma_delimited(input_number1, input_number2):
    return input_number1 + input_number2

def process_two_numbers_newline_delimited(input_number1, input_number2):
    return input_number1 + input_number2

def process_three_numbers(input_string):
    if "," in input_string:
        numbers = input_string.split(",")
    elif "\n" in input_string:
        numbers = input_string.split("\n")
    else:
        return None
    return sum(map(int, numbers))

def ThrowExceptionForNegativeNumbers(input_number):
    if input_number < 0:
        raise ValueError("Negatives not allowed")
    return input_number

def process_numbers_with_custom_delimiters(input_string):
    if input_string.startswith("//"):
        delimiter_part, input_string = input_string.split("\n", 1)
        delimiters = re.findall(r'\[(.*?)\]', delimiter_part)
        if not delimiters:
            delimiters = [delimiter_part[2:]]
        for delimiter in delimiters:
            input_string = input_string.replace(delimiter, ",")
    else:
        input_string = input_string.replace("\n", ",")
    numbers = map(int, input_string.split(","))
    return sum(numbers)