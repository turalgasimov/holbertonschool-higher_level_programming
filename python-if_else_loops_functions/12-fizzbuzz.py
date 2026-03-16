#!/usr/bin/python3

def fizzbuzz():
    for i in range(101):
        s = ', '
        if i == 0:
            print(0, end=s)
        if i == 100:
            s = '\n'
        if i % 3 == 0:
            print("Fizz", end=s)
        elif i % 5 == 0:
            print("Buzz", end=s)
        elif i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz", end=s)
        else:
            print(i, end=s)
