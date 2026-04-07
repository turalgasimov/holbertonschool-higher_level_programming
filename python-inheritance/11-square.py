#!/usr/bin/python3
'''This module is child class of Rectangle.'''
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    '''Is child of BaseGeometry.'''

    def __init__(self, size):
        super().integer_validator("size", size)

        self.__size = size

    def area(self):
        return self.__size ** 2

    def __str__(self):
        return f'[Square] {self.__size}/{self.__size}'
