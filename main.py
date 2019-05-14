import re

numerals = {
    "numbers": ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight",
                "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen",
                "seventeen", "eighteen", "nineteen"],
    "tens": ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy",
             "eighty", "ninety"],
    "powers": {
        100: "hundred",
        1000: "thousand",
        1000000: "million"}}

operations = {
    "+": "plus",
    "-": "minus",
    "*": "multiply",
    "/": "divide",
    "=": "equals",
}


def convert_num_to_word(num):
    if num < 20:
        return numerals["numbers"][num]
    elif num < 100:
        high_digit = numerals["tens"][num // 10]
        low_digit = "" if num % 10 == 0 else "-" + \
            numerals['numbers'][num % 10]
        return high_digit + low_digit
    else:
        highest_power = max(
            [power for power in numerals['powers'].keys() if power <= num])
        return convert_num_to_word(num // highest_power) + " " + numerals["powers"][highest_power] + " " \
            + ("" if num %
               highest_power == 0 else convert_num_to_word(num %
                                                           highest_power))


def string_contains_error(splited_string):
    max_num = max(numerals["powers"].keys())
    if splited_string[0] in operations or \
            splited_string[len(splited_string) - 1] in operations:
        return True
    for i in splited_string:
        print()
        if (not i.isdigit() and i not in operations.keys()) or \
                (i.isdigit() and int(i) > max_num * 10):
            return True
    return False


def convert_expression_to_words(string):
    string = string.replace(" ", "")  # remove all whitespaces
    splited_string = re.findall('[0-9]+|.', string)

    if string_contains_error(splited_string):
        return "Invalid input"

    result = []
    for i in splited_string:
        if i in operations.keys():
            result.append(" " + operations[i] + " ")
        else:
            result.append(convert_num_to_word(int(i)))

    return "".join(result)
