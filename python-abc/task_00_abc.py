#!/usr/bin/python3
from abc import ABC, abstractmethod


class Animal(ABC):
    """
    Abstract class Animal with an abstract method sound.
    """
    @abstractmethod
    def sound(self):
        """
        Abstract method to be implemented by subclasses.
        """
        pass


class Dog(Animal):
    """
    Dog class that implements the sound method from Animal.
    """
    def sound(self):
        """
        Returns the sound of the dog.
        """
        return "Bark"


class Cat(Animal):
    """
    Cat class that implements the sound method from Animal.
    """
    def sound(self):
        """
        Returns the sound of the cat.
        """
        return "Meow"
