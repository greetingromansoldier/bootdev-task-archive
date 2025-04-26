# Rectangle Edges

We previously created a `Rectangle` class with private coordinates `__x1`, `__y1`, `__x2`, and `__y2`. Now, we want to write **getter methods** to determine the rectangle’s edges.

---

## Assignment

1. **Getter Methods**
   - `get_left_x()`
   - `get_right_x()`
   - `get_top_y()`
   - `get_bottom_y()`

   **Note**: Since `x1` or `x2` could represent the left or right edge (and similarly for `y1`/`y2`), you’ll likely use the built-in `min()` and `max()` functions (or comparison operators) to figure out which value corresponds to left/right/top/bottom.

2. **`__repr__` Method**
   - We will learn about and implement this later in the chapter. For now, focus on the edge methods.
