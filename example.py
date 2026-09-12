"""
Demo script: create rectangles/squares and show off their methods.

Usage:
    python example.py
"""

from shapes import Rectangle, Square

if __name__ == "__main__":
    rect = Rectangle(10, 5)
    print(rect)
    print("Area:", rect.get_area())
    print("Perimeter:", rect.get_perimeter())
    print("Diagonal:", round(rect.get_diagonal(), 2))
    print(rect.get_picture())

    sq = Square(9)
    print(sq)
    sq.set_side(4)
    print("After resizing:", sq)
    print(sq.get_picture())

    rect.set_height(10)
    rect.set_width(10)
    print("Amount of 4x4 squares inside a 10x10 rectangle:", rect.get_amount_inside(Square(4)))
