# Assignment

At Doc2Doc, we need better internal debugging tools. **Complete the `args_logger` function.** It takes a variable number of positional and keyword arguments and prints them to the console.

1.  Print each positional argument *sequentially* using numbers and periods as the prefixes, starting with `1`. For example:

    ```python
    args_logger("what's", "up", "doc")
    ```

    prints to the console:

    ```
    1. what's
    2. up
    3. doc
    ```

2.  Print each keyword argument *alphabetically by key* using asterisks (`*`) as the prefix with a colon (`:`) in between. For example:

    ```python
    args_logger("hi", "there", age=17, date="July 4 1776")
    ```

    prints to the console:

    ```
    1. hi
    2. there
    * age: 17
    * date: July 4 1776
    ```

Use the `sorted()` function to get the order right.

## Tips

*   Don't feel guilty about using loops.
*   `kwargs` is a dictionary, not a list. My recommendation is to use the `.items()` method to get its key-value pairs as a list of tuples, then sort that list before printing.
