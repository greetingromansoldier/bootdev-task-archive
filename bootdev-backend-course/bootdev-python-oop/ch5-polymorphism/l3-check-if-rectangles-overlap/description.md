# Check If Rectangles Overlap

## Assignment

We want to write the `overlaps(self, rect)` method to determine if **this** rectangle overlaps a given rectangle, `rect`.

1. **Return Value**
   - Return `True` if **any part** of this rectangle overlaps or touches `rect`.
   - Return `False` otherwise.

2. **Overlap Conditions**
   Let **A** be **this** rectangle and **B** be the rectangle passed in (`rect`). To overlap or touch, **all** of these conditions must be true:

   1. A's **left side** is on or to the left of B's **right side**
      \[
      A_{\text{left}} \le B_{\text{right}}
      \]
   2. A's **right side** is on or to the right of B's **left side**
      \[
      A_{\text{right}} \ge B_{\text{left}}
      \]
   3. A's **top side** is on or above B's **bottom side**
      \[
      A_{\text{top}} \ge B_{\text{bottom}}
      \]
   4. A's **bottom side** is on or below B's **top side**
      \[
      A_{\text{bottom}} \le B_{\text{top}}
      \]

If all four conditions are satisfied, the rectangles **overlap** or touch along the edges; otherwise, they do not.
