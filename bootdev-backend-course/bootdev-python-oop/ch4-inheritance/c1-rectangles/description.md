# Rectangles and Squares

You discovered that to properly calculate army formations in the game, you need to be able to get the **area** and **perimeter** of squares and rectangles of various sizes.

---

## Challenge

Finish implementing the empty methods of the `Rectangle` and `Square` classes. Remember:
- All squares are rectangles, but not all rectangles are squares.
- **Due to inheritance of methods**, the `Square` class should only need to implement the `__init__` method.

### 1. `Rectangle` Class
- **`__init__(self, length, width)`**: Sets the rectangle's length and width.
- **`get_area(self)`**: Returns the area of the rectangle.
- **`get_perimeter(self)`**: Returns the perimeter of the rectangle.

### 2. `Square` Class
- **Inherits** from `Rectangle`.
- Only needs to implement `__init__(self, side)`, because:
  - A square’s length and width are the **same**.
  - Area and perimeter methods can be **inherited** from the `Rectangle` class.
