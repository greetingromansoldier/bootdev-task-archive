# Assignment

Doc2Doc needs a good logging system so that users and developers alike can see what's going on under the hood. **Complete the `get_logger` function.**

It takes a `formatter` function as a parameter and returns a *new function*. Steps:

1.  Define a new function, `logger`, inside `get_logger` (see `self_math` above as an example). It accepts two strings. You can just name them `first` and `second` if you like.
2.  The `logger` function should *not* return anything. It should simply `print` the result of calling the given `formatter` function with the `first` and `second` strings as arguments.
3.  Return the new `logger` function for the test suite to use.

# Tip

The `colon_delimit` and `dash_delimit` functions are "formatters" that will be passed into our `get_logger` function by the tests. You don't need to touch them, but it's important to understand that when you call `formatter()` in the `get_logger` function, you're calling one of these functions.
