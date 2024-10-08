#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return 0

    roman_dict = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000
    }

    result = 0
    length = len(roman_string)

    for i in range(length):
        if i + 1 < length and \
                roman_dict[roman_string[i]] < roman_dict[roman_string[i + 1]]:
            result -= roman_dict[roman_string[i]]
        else:
            result += roman_dict[roman_string[i]]

    return result
