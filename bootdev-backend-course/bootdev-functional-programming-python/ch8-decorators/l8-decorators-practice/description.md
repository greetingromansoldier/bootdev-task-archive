## Assignment

Complete the `replacer` function.

1.  [ ] It takes as input two strings, `old` and `new`, and returns a function, `replace`.
2.  [ ] `replace` takes an input function, `decorated_func`, and returns a `wrapper` function.
3.  [ ] `wrapper` takes as input a string `text`. It uses `.replace()` string method to replace instances of `old` with `new` in the `text`. Then it returns the result of passing the modified `text` to the `decorated_func`.
4.  [ ] Use a series of the `replacer` function to decorate `tag_pre`. Pass the following pairs of strings to these decorators to encode the escape sequences:
    1.  [ ] Replace `"&"` with `"&"`
    2.  [ ] Replace `"<"` with `"<"`
    3.  [ ] Replace `">"` with `">"`
    4.  [ ] Replace `"""` with `"""`
    5.  [ ] Replace `"'"` with `"'"`
