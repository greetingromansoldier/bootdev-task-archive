# Wizard Class

## Requirements

1. **Inheritance**
   - The `Wizard` class should inherit from the `Hero` class.

2. **Constructor Setup**
   - Set the hero’s `name` and `health` through the `Hero` constructor.
   - Accept a third parameter for the private `__mana` variable.

3. **`cast(self, target)` Method**
   - Takes a target hero as input.
   - If there is **less than 25 mana** left, raise a `not enough mana` exception.
   - Otherwise, **remove 25 mana** from the wizard and **deal 25 damage** to the target hero.
