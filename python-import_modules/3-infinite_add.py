#!/usr/bin/python3

import sys

if __name__ == "__main__":
    if len(sys.argv) == 1:
        print(0)
    sum = 0
    for i in range(1, len(sys.argv)):
        sum += int(sys.argv[i])
    print(sum)
