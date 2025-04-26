# code before changes:

# def find_longest_word(document, longest_word=""):
#     pass

# actual code:

# solve a small problem:
#     - calcualate len of one word

def find_longest_word(document, longest_word=""):
    splitted_doc = document.split(" ")
    if len(document) > 0:
        if len(splitted_doc[0]) > len(longest_word):
            longest_word = splitted_doc[0]
        result = find_longest_word(" ".join(splitted_doc[1:]), longest_word)
        longest_word= result
        return longest_word
    else:
        return longest_word
