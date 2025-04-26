# Filter Command

In Doc2Doc, users are asking for a filtering feature. They want a command that has dynamic options so they can work as quickly as possible.

# Assignment

Complete the `get_filter_cmd` function. It takes two functions as input, `filter_one` and `filter_two`, and returns a function, `filter_cmd`.

`filter_cmd` should take as input:

*   a string `content` to be filtered
*   an `option` with a default value of `--one`.

The `filter_cmd` should filter and return the `content` according to the input `option`. Do not use the builtin `filter` function.

1.  If `--one`, use `filter_one`
2.  If `--two`, use `filter_two`
3.  If `--three`, use `filter_one` first, then use `filter_two`
4.  If another option is passed, raise an exception, `"invalid option"`
