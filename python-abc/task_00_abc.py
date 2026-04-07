#!/usr/bin/python3
'''This module contains ABC class Animal'''
from abc import ABC


class Animal(ABC):
    '''Animal class'''

    @abstractmethod
    def sound(self):
        ...

class Dog(Animal):
    '''Dog class'''
    def sound(self):
        return 'Bark'

class Cat(Animal):
    '''Cat class'''
    def sound(self):
        return 'Meow'
