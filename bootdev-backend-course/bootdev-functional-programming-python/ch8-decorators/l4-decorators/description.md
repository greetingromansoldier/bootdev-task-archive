## Assignment

Complete the `markdown_to_text_decorator` function. It can decorate a function with *any number of string arguments*, no matter if they're positional or keyword args. It will run the decorated function, but first strip out any Markdown heading symbols (see below for an explanation of Markdown headings).

It should `return` a `wrapper` function that takes `*args` and `**kwargs`. The wrapper should:

1.  Map the `*args` to a new `list` where each string is converted to plain text using `convert_md_to_txt`.
2.  Map the `**kwargs` to a new `dictionary` where each "value" is converted to plain text using `convert_md_to_txt`. The "key" should remain the same.
    *   Use the `.items()` dictionary method to pass a list of tuples of `key-value` pairs to map.
    *   Create a function for `map` which changes the `value` of an item tuple with `convert_md_to_txt`.
3.  Return the result of calling the decorated function with the new arguments.

## Tips

*   Take a look at the editor's `formatters.py` file tab to see what the formatter functions do. What arguments are they expecting? You can use `*` tuple unpacking and `**` dictionary unpacking operators to pass variables as the correct arguments.
*   The provided `convert_md_to_txt` function takes a string of Markdown text and returns a string of text with any "heading" symbols removed. For example:

| Input                    | Output                   |
| :----------------------- | :----------------------- |
| `# This is a heading`    | `This is a heading`    |
| `## This is also a heading` | `This is also a heading` |
| `This is not a heading`  | `This is not a heading`  |
| `* This is also not a heading` | `* This is also not a heading` |
