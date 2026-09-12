"""
Polygon Area Calculator

A Rectangle class (with a Square subclass) for computing area,
perimeter, diagonal length, and a simple ASCII-art representation.
"""

import math


class Rectangle:
    """A rectangle defined by its width and height."""

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def set_width(self, width):
        """Update the width."""
        self.width = width

    def set_height(self, height):
        """Update the height."""
        self.height = height

    def get_area(self):
        """Return the area (width * height)."""
        return self.width * self.height

    def get_perimeter(self):
        """Return the perimeter (2 * (width + height))."""
        return 2 * (self.width + self.height)

    def get_diagonal(self):
        """Return the length of the diagonal."""
        return math.sqrt(self.width ** 2 + self.height ** 2)

    def get_picture(self):
        """
        Return a string of asterisks representing the rectangle's shape,
        one row per unit of height, one '*' per unit of width.

        Returns "Too big for picture." instead if either side exceeds 50,
        since a picture that large wouldn't be practical to print.
        """
        if self.width > 50 or self.height > 50:
            return "Too big for picture."
        picture = ""
        for _ in range(self.height):
            picture += "*" * self.width + "\n"
        return picture

    def get_amount_inside(self, shape):
        """
        Return how many times `shape` could fit inside this rectangle,
        based on total area (not a physical packing arrangement).
        """
        return self.get_area() // shape.get_area()

    def __repr__(self):
        return f"Rectangle(width={self.width}, height={self.height})"


class Square(Rectangle):
    """A square is a rectangle whose width and height are always equal."""

    def __init__(self, side):
        super().__init__(side, side)

    def set_width(self, width):
        """Update the side length (keeps width and height equal)."""
        self.width = width
        self.height = width

    def set_height(self, height):
        """Update the side length (keeps width and height equal)."""
        self.width = height
        self.height = height

    def set_side(self, side):
        """Update the side length directly."""
        self.width = side
        self.height = side

    def __repr__(self):
        return f"Square(side={self.width})"
