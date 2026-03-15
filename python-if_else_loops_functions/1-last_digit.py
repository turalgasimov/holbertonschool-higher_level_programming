#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
# YOUR CODE HERE

lastDigit = number % 10
if number < 0:
    lastDigit += -10
str = (
    "and is greater than 5" 
    if lastDigit > 5 
    else "and is less than 6 and not 0" 
    if lastDigit < 6 and lastDigit != 0 else "and is 0")

print(f'Last digit of {number} is {lastDigit} {str}')
