#!/usr/bin/python3
"""
This module defines a Fish, Bird, and FlyingFish class
to demonstrate multiple inheritance and method resolution order (MRO).
"""


class Fish:
    """
    A class representing a Fish.

    Methods:
    - swim: Prints a message indicating the fish is swimming.
    - habitat: Prints the habitat where the fish lives.
    """
    def swim(self):
        """
        Prints a message indicating the fish is swimming.
        """
        print("The fish is swimming")

    def habitat(self):
        """
        Prints the habitat where the fish lives.
        """
        print("The fish lives in water")


class Bird:
    """
    A class representing a Bird.

    Methods:
    - fly: Prints a message indicating the bird is flying.
    - habitat: Prints the habitat where the bird lives.
    """
    def fly(self):
        """
        Prints a message indicating the bird is flying.
        """
        print("The bird is flying")

    def habitat(self):
        """
        Prints the habitat where the bird lives.
        """
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """
    A class representing a FlyingFish, inheriting from both Fish and Bird.
    
    Overrides:
    - swim: Prints a message indicating the flying fish is swimming.
    - fly: Prints a message indicating the flying fish is soaring.
    - habitat: Prints the habitat where the flying fish lives.
    """
    def swim(self):
        """
        Prints a message indicating the flying fish is swimming.
        """
        print("The flying fish is swimming!")

    def fly(self):
        """
        Prints a message indicating the flying fish is soaring.
        """
        print("The flying fish is soaring!")

    def habitat(self):
        """
        Prints the habitat where the flying fish lives.
        """
        print("The flying fish lives both in water and the sky!")
