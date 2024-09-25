#!/usr/bin/python3
"""
This module defines mixins for swimming and flying behaviors
and a Dragon class that can swim, fly, and roar.
The Dragon class demonstrates the use of multiple inheritance through mixins.
"""


class SwimMixin:
    """
    Mixin class that provides swimming ability.

    Methods:
    --------
    swim() -> None:
        Prints a message indicating that the creature swims.
    """
    def swim(self):
        """
        Prints a message indicating the creature swims.
        """
        print("The creature swims!")


class FlyMixin:
    """
    Mixin class that provides flying ability.

    Methods:
    --------
    fly() -> None:
        Prints a message indicating that the creature flies.
    """
    def fly(self):
        """
        Prints a message indicating the creature flies.
        """
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """
    Dragon class that can swim, fly, and roar.

    Inherits from SwimMixin and FlyMixin to demonstrate multiple behaviors.

    Methods:
    --------
    roar() -> None:
        Prints a message indicating that the dragon roars.
    """
    def roar(self):
        """
        Prints a message indicating the dragon roars.
        """
        print("The dragon roars!")
