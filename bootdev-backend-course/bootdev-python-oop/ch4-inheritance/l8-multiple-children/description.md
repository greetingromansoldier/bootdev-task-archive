# Archer Class

## Requirements

1. **Inheritance**
   - The `Archer` class should inherit from the `Hero` class.

2. **Constructor Setup**
   - Set the hero’s name and health through the `Hero` constructor.
   - Accept a third parameter for the private `__number_of_arrows` variable.

3. **`shoot(self, target)` Method**
   - Takes a target hero as input.
   - If there are **no arrows** left, raise a `not enough arrows` exception.
   - Otherwise, **remove one arrow** and **deal 10 damage** to the target hero.
