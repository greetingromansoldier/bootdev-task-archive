# Bringing It Together in the Dragon Class

Let's bring all we've done together in the `Dragon` class. The `Dragon` class should override the `Unit` class's `in_area` method. Instead of checking if the center position of the Dragon is in the given area, we'll check if its big dragon body (hitbox) overlaps with the given area.

> **Note:** Methods in parent classes often use `pass` to signal they should be overridden in child classes. To override, create a method with the same name in the child class.

## Assignment

1.  - [ ] **Complete the Dragon's constructor:**
    1.  - [ ] Add a private data member: `__hit_box` that is a `Rectangle` object.
    2.  - [ ] Use the provided height, width, and center position (`pos_x`, `pos_y`) of the dragon to create the hitbox.
        *   *(Hint: You'll likely need to calculate the corner coordinates based on the center, width, and height - see Tips below)*
2.  - [ ] **Override the `in_area` method:**
    1.  - [ ] Create a new `Rectangle` object representing the query area using the given corner positions (passed as arguments to `in_area`).
    2.  - [ ] Use the query rectangle's `overlaps` method to check if the Dragon's `self.__hit_box` overlaps with it.
    3.  - [ ] Return the resulting boolean value.

## Example Hitbox

*(See original image for visual diagram)*

The example shows a hitbox represented as a rectangle centered at coordinates `(pos_x = 2, pos_y = 1)`. The `width` extends horizontally from the center, and the `height` extends vertically.

## Tips: Calculating Hitbox Corners from Center

To create the `Rectangle` object for the hitbox, you usually need corner coordinates (like top-left and bottom-right, or all four corners depending on the `Rectangle` class implementation). You can calculate these from the center (`pos_x`, `pos_y`), `width`, and `height`:

*   **Right Side (x-coordinate):** `pos_x + (width / 2)`
*   **Left Side (x-coordinate):** `pos_x - (width / 2)`
*   **Top Side (y-coordinate):** `pos_y + (height / 2)`
*   **Bottom Side (y-coordinate):** `pos_y - (height / 2)`

Combine these to get the necessary corner points for your `Rectangle` constructor.
