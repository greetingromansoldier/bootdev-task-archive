# Assignment: Dragon String Formatting
#programming #python #oop #string-formatting #assignment

Dragons are egotistical creatures; let's give them a great format for announcing their presence in "Age of Dragons".

## Task

When `print()` is called on an instance of a `Dragon`, the string `I am {0}, the {1} dragon` should be printed.

## Placeholders

-   `{0}` is the **name** of the dragon.
-   `{1}` is the **color** of the dragon.

## Hint

You likely need to implement the `__str__` or `__repr__` dunder method on the `Dragon` class to control how its instances are represented as strings, especially when used with `print()`. `__str__` is generally preferred for user-friendly output.
