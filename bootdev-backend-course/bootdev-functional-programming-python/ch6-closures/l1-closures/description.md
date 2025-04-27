
# Assignment

Doc2Doc keeps track of how many words are in a collection of documents.

Complete the `word_count_aggregator` function. It should return a function that calculates the number of words in its input (`doc`, a string). It should then add that number to an *enclosed* `count` value and return the new `count`. In other words, it keeps a running total of the `count` variable within a closure.



# Tip

I used `.split()` to count the number of words in the doc string.
