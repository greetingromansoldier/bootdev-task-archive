# Sprint

In **Age of Dragons**, humans can "sprint" to move twice as fast. However, sprinting requires `__stamina`. Each time a human sprints, it loses stamina. Once it is out of stamina, it can no longer sprint.

---

## Assignment

### 1. Complete the Private Helper Methods
1. **`__raise_if_cannot_sprint()`**  
   - Raise an exception:  
     ```python
     raise Exception("not enough stamina to sprint")
     ```
     if the human is out of stamina.

2. **`__use_sprint_stamina()`**  
   - Remove one stamina from the human.

### 2. Implement the Sprint Methods
For each of the sprint methods (e.g., `sprint_right()`, `sprint_left()`, `sprint_up()`, `sprint_down()`):
1. Raise an error if there isn't enough stamina to sprint (use `__raise_if_cannot_sprint()`).
2. Use the stamina needed to sprint (call `__use_sprint_stamina()`).
3. Move twice in the intended direction.
