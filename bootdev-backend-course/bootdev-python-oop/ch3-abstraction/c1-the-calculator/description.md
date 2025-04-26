# The Calculator

## Assignment

Complete the `Calculator` class methods. They should perform their respective mathematical computations. The "left-hand side" of each operation should be the current value of the `result` variable. The "right-hand side" of each operation will be the value passed in.

1. **Create a private instance variable** called `__result` initialized to `0`.

2. **Create the following math methods**:
   - **`add(self, a)`**
   - **`subtract(self, a)`**
   - **`multiply(self, a)`**
   - **`divide(self, a)`**  
     &nbsp;&nbsp;If the user attempts to divide by 0, raise a `ValueError` with `"cannot divide by zero"`.
   - **`modulo(self, a)`**  
     &nbsp;&nbsp;If the user attempts to divide by 0, raise a `ValueError` with `"cannot divide by zero"`.
   - **`power(self, a)`**
   - **`square_root(self)`**  
     &nbsp;&nbsp;Remember that the square root of a number can be calculated by raising it to the power of `0.5`.

3. **Create the helper methods**:
   - **`clear(self)`**  
     &nbsp;&nbsp;Reset the `__result` variable to `0`.
   - **`get_result(self)`**  
     &nbsp;&nbsp;Return the current value stored in the calculator's private `__result` variable.

---

## Hints

- For the **power** and **square_root** operations, search your spellbook for how to use exponents in Python.
- To calculate the square root of a number, you can raise it to the power of `0.5`.
