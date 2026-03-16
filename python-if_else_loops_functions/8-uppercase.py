#!/usr/bin/python3

def uppercase(str):
    s = ''
    size = len(str)
    if str == '':
        str = ' '
    for i in range(len(str)):
        if i == size - 1:
            s = '\n'
        if ord('a') <= ord(str[i]) <= ord('z'):
            print('{}'.format(chr(ord(str[i]) - 32)), end=s)
        else:
            print(str[i], end=s)

uppercase("Best School 98 Battery street")
uppercase("")
uppercase(" ")