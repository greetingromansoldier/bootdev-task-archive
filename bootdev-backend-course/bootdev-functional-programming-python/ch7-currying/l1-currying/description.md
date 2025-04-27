# Assignment

In Doc2Doc, depending on the type of text file we're working with, we sometimes need to transform the font size of the text when it comes time to render it on the screen.

Fix the `converted_font_size` function. We are using a 3rd party code library that expects our function to be a curried series of functions that each take a single argument.

*   `converted_font_size` should just take a single argument, `font_size` and return a function that takes a single argument, `doc_type`. That function should return the `font_size` multiplied by the appropriate value for the given `doc_type`.

# Tip

You can always `Reset` the code to see the proper `font_size` multipliers if you accidentally change them.
