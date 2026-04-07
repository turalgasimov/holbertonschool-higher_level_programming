#!/usr/bin/python3
'''This module is child class of BaseGeometry.'''


class Rectangle(7-base_geometry.BaseGeometry):
    '''Is child of BaseGeometry.'''

    def __init__(self, width, height):
        if super().integer_validator(width):
            self.__width = width
        if super().integer_validator(height):
            self.__height = height
