# Longest Word

In Doc2Doc, we have a search function to find the longest word in a document.

## Assignment

Complete the `find_longest_word` function without a loop. It accepts string inputs, `document`, and optional `longest_word`, which is the current longest word and defaults to an empty string.

*   Check if the first word is longer than the current `longest_word`, then recur for the rest of the document.
*   Ensure there are no potential index errors.

*Assume that a "word" means a series of any consecutive non-whitespace characters. For example,* `longest_word("How are you?")` *should return the string* `"you?"`.
