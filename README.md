# Polygon Area Calculator

A small object-oriented Python project modeling a `Rectangle` class
(and a `Square` subclass) with methods to compute area, perimeter,
diagonal length, and a simple ASCII-art picture of the shape.

## Features

- `Rectangle` — area, perimeter, diagonal length, and an ASCII picture
  made of asterisks
- `Square` — inherits from `Rectangle`; keeps width and height in sync
  automatically
- `get_amount_inside()` — calculates how many of one shape's area fit
  inside another

## Project structure

```
polygon-area-calculator/
├── shapes.py               # Rectangle and Square classes
├── example.py                # Demo script
├── tests/
│   └── test_shapes.py          # Test suite (pytest)
├── requirements.txt
├── .gitignore
├── LICENSE
└── README.md
```

## Installation

```bash
git clone https://github.com/<your-username>/polygon-area-calculator.git
cd polygon-area-calculator
pip install -r requirements.txt   # only needed to run the tests
```

No external libraries are required to run the project itself — it only
uses Python's standard library (`math`).

## Usage

```python
from shapes import Rectangle, Square

rect = Rectangle(10, 5)
print(rect.get_area())        # 50
print(rect.get_perimeter())   # 30
print(rect.get_picture())

sq = Square(9)
sq.set_side(4)
print(sq)                     # Square(side=4)
```

Or run the included demo:

```bash
python example.py
```

## Running the tests

```bash
pytest
```

16 tests cover area/perimeter/diagonal calculations, the ASCII picture
(including the "too big" case), `Square`'s inherited behavior, and
`get_amount_inside()`.

## Bug fixed from the original version

`get_amount_inside()` originally calculated a **grid-fit** answer —
`(self.width // shape.width) * (self.height // shape.height)` — instead
of comparing total areas. That gives a different, and usually smaller,
result than the intended calculation.

For example, fitting a 3×3 square inside a 10×15 rectangle:
- **Grid-fit (old, buggy) result:** `(10 // 3) * (15 // 3)` = `3 * 5` = **15**
- **Area-based (correct) result:** `150 // 9` = **16**

The fixed version uses `self.get_area() // shape.get_area()`, matching
the standard definition of "how many times could this shape's area fit
inside mine."

## Known limitations / next steps

This is a learning project, so it's intentionally simple. Ideas for
extending it:

- Add a `Circle` or `Triangle` class to broaden the shape hierarchy.
- Validate that width/height/side are positive numbers.
- Let `get_picture()` accept a custom fill character instead of always
  using `*`.

## License

This project is licensed under the MIT License — see [LICENSE](LICENSE)
for details.
