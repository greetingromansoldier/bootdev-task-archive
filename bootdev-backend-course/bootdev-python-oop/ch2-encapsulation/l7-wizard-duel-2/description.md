---
## Assignment

### Complete the following methods

1. **Create the `cast_fireball` method**
   - If there isn’t enough mana to cast a fireball (see `fireball_cost` at the top of the file), raise an `Exception` with the message:
     ```
     <wizard_name> cannot cast fireball
     ```
   - If the wizard has enough mana, reduce their mana by the `fireball_cost` and call `get_fireballed` on the target wizard.

2. **Create the `is_alive` method**
   - Returns `True` if the wizard’s health is greater than 0.
   - Returns `False` otherwise.
