## Assignment

The creator of Doc2Doc is a huge fan of `palindromes` for some nerdy reason. Add a feature to check if a word is a palindrome.

1.  [ ] Import the `lru_cache` function from the `functools` module and use it to decorate the incomplete `is_palindrome` function.
2.  [ ] Complete the `is_palindrome` function. It takes as input a `word` string and returns `True` if the word is a palindrome (such as "racecar"), or `False` otherwise.

Try to use recursion. Check the outer characters first, then move inwards until you reach the base case or find the word is not a palindrome.
