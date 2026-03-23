#!/usr/bin/python3
def roman_to_int(roman_string):
    if type(roman_string) is not str:
        return 0

    roman_dict = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }

    sum = 0
    for i in range(len(roman_string)):
        num = roman_dict[roman_string[i]]
        if (
            (i < len(roman_string) - 1)
        and (num < roman_dict[roman_string[i+1]])
        ):
            num *= -1
        sum += num

    return sum
