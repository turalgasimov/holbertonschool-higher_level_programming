#!/usr/bin/python3

def print_last_digit(number):
    lastDigit = number % 10
    if number < 0:
        lastDigit += -10
    print('{}'.format(lastDigit), end='')
    return(lastDigit)
