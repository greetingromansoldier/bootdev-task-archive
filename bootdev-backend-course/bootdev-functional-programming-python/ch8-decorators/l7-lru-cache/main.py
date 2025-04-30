# code before changes:

# ?

# ?
# def is_palindrome(word):
#     pass

# actual code:

from functools import lru_cache

@lru_cache
def is_palindrome(word):
    if len(word) <= 1: 
        return True
    if word[0] != word[-1]:
        return False
    trimmered_word = word[1:-1]
    return is_palindrome(trimmered_word)



