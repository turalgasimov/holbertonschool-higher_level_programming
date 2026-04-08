#!/usr/bin/python3
'''This module contains ABC class Shape'''
from abc import ABC, abstractmethod
import math as m


class Shape(ABC):
    '''abstract class Shape'''

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

class Circle(ABC):
    '''class Circle'''

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return m.pi * (self.radius ** 2)

    def perimeter(self):
        return self.radius * 2 * m.pi

class Rectangle(ABC):
    '''class Rectangle'''

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

def shape_info(self):
    '''prints area and perimeter'''

    print(f'Area: {self.area()}')
    print(f'Perimeter: {self.perimeter()}')

if __name__ == "__main__":
    # Testing the functionality
    circle = Circle(radius=1)
    rectangle = Rectangle(width=1, height=2)

    shape_info(circle)
    shape_info(rectangle)
