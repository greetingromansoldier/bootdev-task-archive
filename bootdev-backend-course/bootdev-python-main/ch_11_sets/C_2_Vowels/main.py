# code before changes:

# def count_vowels(text):
#     pass

# assignment:

# Complete the count_vowels function. 
# It should take a string and return a count of the number of vowels within the given string, and a set of its unique vowels.

# For this challenge, we are only interested in the 5 vowels: a, e, i, o, u, and their capitalized versions.
# In addition, treat uppercase and lowercase vowels as separate. 
# For example, "A" and "a" are not the same.

# actual code:

def count_vowels(text):
    expected_vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
    count_vowels = 0
    vowels_set = set()
    for letter in text:
        if letter in expected_vowels:
            count_vowels += 1
            vowels_set.add(letter)
    return count_vowels, vowels_set    

# мне как-то неочевидно, почему цикл for перебирает здесь текст по буквам, нооо возможно так и должно быть??
# например, если надо перебирать по словам, то инпут должен быть не str, а список
