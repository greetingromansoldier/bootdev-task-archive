# Organize Keywords

By organizing keywords, documents are mapped to their relevant terms, enabling users to quickly view the keywords associated with each document. It also reduces the computational overhead of repeatedly searching for the same terms, improving the performance and responsiveness of Doc2Doc. This is useful for notebooking, research and project management.

# Assignment

Complete the `find_keywords` function. It takes as input a `document` string and returns a list of the keyword substrings in the `document`.

The `keywords` list is being modified at the start of code execution. Turn `find_keywords` into a pure function that does not rely on a global variable.

1.  Move the `keywords` list inside the `find_keywords` function so changes to the global scope do not change this list.
2.  Filter the `keywords` to create a new list containing only the keyword substrings *in* the `document`.
3.  Be sure to return the found keyword substrings as a list.

> **⚠️ Warning:** The keyword search is **case-insensitive**. This means that "Lambda" and "lambda" are the same word.

Fix the `map_keywords` function. It takes a string `document` input and a dictionary `document_map` input, and returns a list of `keywords` substrings found in the `document` and a dictionary `document_map` with the document added if needed. The `document_map` dictionary has `document` strings as keys, and their values are a list of `keywords` found in the key string, in the order they appear in the `keywords` list.

1.  Do not modify or return the actual input `document_map`.
2.  If the document is already `in` the document map, return its keywords and the `document_map` copy.
3.  Use `find_keywords` to get the keyword substrings in the `document`.
4.  Add the `document` and its keyword substrings to the `document_map` copy.
5.  Return the `document`'s keyword substrings and the `document_map` copy.

# Tip

Check the test suite to understand how variables are being changed in the global scope.
