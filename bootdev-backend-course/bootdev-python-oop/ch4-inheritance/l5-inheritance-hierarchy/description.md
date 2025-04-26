# Crossbowman and Updated Archer

Let's add a new game unit: **Crossbowman**. A crossbowman is always an archer, but not all archers are crossbowmen. Crossbowmen have several arrows, but they also have an additional method: `triple_shot()`.

---

## Updated Archer Class

1. **Add `use_arrows(self, num)` Method**
   - Removes `num` arrows from the archer’s `__num_arrows` property.
   - If there aren’t enough arrows to remove, raise a `not enough arrows` exception.

---

## Crossbowman Class

1. **Constructor**
   - Inherits from `Archer`, so call the parent’s constructor (`super().__init__`) to set up inherited properties (e.g., `name`, `__num_arrows`).

2. **`triple_shot(self, target)` Method**
   - Uses **3** arrows (by calling the new `use_arrows` method from `Archer`).
   - Takes a `target` (another `Human` object) as a parameter.
   - Returns the string:
     ```plaintext
     "{} was shot by 3 crossbow bolts"
     ```
     where `{}` is replaced by the name of the `Human` that was shot.
