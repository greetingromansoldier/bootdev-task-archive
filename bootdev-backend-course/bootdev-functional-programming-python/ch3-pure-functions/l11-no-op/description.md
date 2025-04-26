# Assignment

Complete the `remove_emphasis`, `remove_emphasis_from_line`, and `remove_emphasis_from_word` functions. They are currently no-ops.

`remove_emphasis` is the parent function. It takes a full document with any number of lines and removes any single or double `*` characters that are at the start or end of a word. ([Emphasis](https://www.markdownguide.org/basic-syntax/#emphasis) in markdown)

For example, this:

```
I *love* markdown.
I **really love** markdown.
```

Should become:

```
I love markdown.
I really love markdown.
```

Write the helper functions, they will make the `remove_emphasis` function much easier to write:

*   The `remove_emphasis_from_word` function should remove emphasis from a single word.
*   The `remove_emphasis_from_line` function should split a given line into words and use the function we just created to remove emphasis from each word.

Don't forget to handle newline characters (`\n`) appropriately at the end of lines.

# Tips

For the sake of practice, try it without the `.replace()` string method. I used some of these built-ins:

*   `str.split`
*   `str.strip`
*   `map`
*   `join`
