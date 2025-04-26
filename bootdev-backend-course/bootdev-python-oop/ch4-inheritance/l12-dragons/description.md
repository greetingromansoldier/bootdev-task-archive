# Dragons and the Game Grid

In **Age of Dragons**, there are many types of units (Orcs, Humans, Goblins, Dragons, etc.). All of these are called "units." Each unit has:
- A position on the game map (Cartesian coordinates).
- A name.

**Dragons** are a special type of unit that can breathe fire, damaging units in a specified area.

---

## Assignment

### 1. `in_area` Method (on `Unit`)

**Signature**: `in_area(self, x1, y1, x2, y2)`

- `(x1, y1)` represents the **bottom-left** corner of a rectangle.
- `(x2, y2)` represents the **top-right** corner of the rectangle.
- Determine if the unit’s position (`pos_x`, `pos_y`) is **within or on the boundary** of this rectangle.
- Return `True` if the unit’s position is inside/on the edge; otherwise, return `False`.

### 2. `breathe_fire` Method (on `Dragon`)

**Signature**: `breathe_fire(self, x, y, units)`

1. The target area is **centered** at `(x, y)`.
2. The area extends `__fire_range` in all directions, **inclusively**.
   - So the rectangle corners would be:
     - Bottom-left: `(x - __fire_range, y - __fire_range)`
     - Top-right: `(x + __fire_range, y + __fire_range)`
3. For each `unit` in the provided `units` list:
   - Check if it is within the blast area (by using the `in_area` method).
   - If yes, add it to a list of units hit by the blast.
4. Return the list of units hit by the blast.

---

## Example

If `__fire_range = 1` and the fire is centered at `(1, 1)`, then the affected rectangle is:
- Bottom-left: `(0, 0)`
- Top-right: `(2, 2)`

Any unit whose position `(pos_x, pos_y)` falls within `(0,0)` to `(2,2)` is hit by the blast.
