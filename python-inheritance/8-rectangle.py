#!/usr/bin/python3
'''This module is child class of BaseGeometry.'''

import BaseGeometry from 7-base_geometry

class Rectangle(BaseGeometry):
    '''Is child of BaseGeometry.'''

    def __init__(self, width, height):
        if super().integer_validator(width):
            self.__width = width
        if super().integer_validator(height):
            self.__height = height
