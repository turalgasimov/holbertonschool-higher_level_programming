#!/usr/bin/python3
"""Define a square based on given info."""


class Square:
    """Defines a square in the system."""
    def __init__(self, size=0, position=(0, 0)):
        """Args: size"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
        self.__position = position

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if not all(isinstance(i, int) for i in value) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")

    def area(self):
        return self.__size**2

    def my_print(self):
        if self.size == 0:
            print()
        else:
            for i in range(self.size):
                print(' ' * position[0])
                for j in range(self.size):
                    print('#', end='')
                print()
