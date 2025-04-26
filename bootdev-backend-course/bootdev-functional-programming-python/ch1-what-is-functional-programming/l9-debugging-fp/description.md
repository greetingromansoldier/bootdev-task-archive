# Assignment

Fix the `format_line` function. It should apply the following transformations in order:

1. Strip whitespace from the beginning and end of the line.
2. Capitalize every character in the line.
3. Remove any periods from the line.
4. Suffix the line with an ellipsis: `words go here...`

*Run the code. You should see that some subtle bugs are present.*

Break up the function to make it easier to debug. Use `print()` statements to see what's going on at each step.

## Tips

Be careful about whitespace! It's easy to miss in console output. I sometimes add a character, like a `|` to the beginning and end of a string to make whitespace more obvious when print debugging.

*   `.replace(old, new)` can be used to replace all instances of a character in a string.
*   `.upper()` capitalizes an entire string, `.capitalize()` capitalizes the first letter.
*   `.strip()` removes whitespace from the beginning and end of a string, `.lstrip()` and `.rstrip()` remove whitespace from the left and right respectively.
