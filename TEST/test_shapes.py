"""
Basic tests for shapes.py.

Run with:
    pytest
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from shapes import Rectangle, Square  # noqa: E402


# --- Rectangle ---

def test_rectangle_area():
    rect = Rectangle(10, 5)
    assert rect.get_area() == 50


def test_rectangle_perimeter():
    rect = Rectangle(10, 5)
    assert rect.get_perimeter() == 30


def test_rectangle_diagonal():
    rect = Rectangle(3, 4)
    assert rect.get_diagonal() == 5.0


def test_rectangle_set_width_and_height():
    rect = Rectangle(10, 5)
    rect.set_width(20)
    rect.set_height(15)
    assert rect.width == 20
    assert rect.height == 15


def test_rectangle_picture_small():
    rect = Rectangle(3, 2)
    assert rect.get_picture() == "***\n***\n"


def test_rectangle_picture_too_big():
    rect = Rectangle(51, 5)
    assert rect.get_picture() == "Too big for picture."

    rect2 = Rectangle(5, 51)
    assert rect2.get_picture() == "Too big for picture."


def test_rectangle_repr():
    rect = Rectangle(10, 5)
    assert repr(rect) == "Rectangle(width=10, height=5)"


# --- Square ---

def test_square_has_equal_sides():
    sq = Square(9)
    assert sq.width == 9
    assert sq.height == 9


def test_square_set_width_updates_both_sides():
    sq = Square(9)
    sq.set_width(4)
    assert sq.width == 4
    assert sq.height == 4


def test_square_set_height_updates_both_sides():
    sq = Square(9)
    sq.set_height(4)
    assert sq.width == 4
    assert sq.height == 4


def test_square_set_side():
    sq = Square(9)
    sq.set_side(6)
    assert sq.width == 6
    assert sq.height == 6


def test_square_repr():
    sq = Square(9)
    assert repr(sq) == "Square(side=9)"


def test_square_is_a_rectangle_and_inherits_its_methods():
    sq = Square(5)
    assert isinstance(sq, Rectangle)
    assert sq.get_area() == 25
    assert sq.get_perimeter() == 20


# --- get_amount_inside ---

def test_get_amount_inside_exact_fit():
    rect = Rectangle(4, 8)
    sq = Square(2)
    assert rect.get_amount_inside(sq) == 8


def test_get_amount_inside_uses_area_not_grid_fit():
    # Regression test for a bug where get_amount_inside used a grid-fit
    # calculation (width // width) * (height // height) instead of
    # comparing total areas. That gave 15 here; the correct, area-based
    # answer is 16.
    rect = Rectangle(10, 15)
    sq = Square(3)
    assert rect.get_amount_inside(sq) == 16


def test_get_amount_inside_with_another_rectangle():
    big = Rectangle(20, 10)
    small = Rectangle(4, 5)
    assert big.get_amount_inside(small) == 10
