#!/usr/bin/python3
'''This module is child class of BaseGeometry.'''
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    '''Is child of BaseGeometry.'''

    def __init__(self, width, height):
        if super().integer_validator("width", width):
            self.__width = width
        if super().integer_validator("height", height):
            self.__height = height

    def area(self):
        return self.__width * self.__height

    def __str__(self):
        return f"{self} {self.__width}/{self.__height}"
