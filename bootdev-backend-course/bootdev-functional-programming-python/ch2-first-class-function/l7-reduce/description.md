# Assignment

Complete the `join` and the `join_first_sentences` functions.

## join()

This is a helper function we'll use in `join_first_sentences`. It takes two inputs:

1.  A `"doc_so_far"` accumulator string. It's similar to the `sum_so_far` variable in the example above.
2.  A `"sentence"` string. This is the next string we want to add to the accumulator.

It returns the result of concatenating the `"doc"` and `"sentence"` strings together, with a period and a space in between. For example:

```python
doc = "This is the first sentence"
sentence = "This is the second sentence"
print(join(doc, sentence))
# This is the first sentence. This is the second sentence
```

## join_first_sentences()

It accepts two arguments:

1.  A list of sentence strings
2.  An integer `n`

It should use the built-in `functools.reduce()` function alongside your `join` function to return a single string: the result of joining the *first* `n` sentences in the list. It should also add a final period (but no trailing space) to the end of the final "reduced" string.

If `n` is zero, just return an empty string.

Use list slicing to get the first `n` sentences. For example:

```python
fruits = ["apple", "banana", "cherry", "date"]
print(fruits[:2])
# ["apple", "banana"]
```

Here's an example of the expected behavior:

```python
joined = join_first_sentences(
    ["This is the first sentence", "This is the second sentence", "This is the third sentence"],
    2
)
print(joined)
# This is the first sentence. This is the second sentence.
```
