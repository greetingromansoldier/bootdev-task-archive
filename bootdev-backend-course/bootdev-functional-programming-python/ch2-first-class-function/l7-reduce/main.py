# code before changes:

# import functools

# def join(doc_so_far, sentence):
#     pass


# def join_first_sentences(sentences, n):
#     pass

# actual code:

import functools

def join(doc_so_far, sentence):
    return doc_so_far + ". " + sentence


def join_first_sentences(sentences, n):
    if n == 0:
        return ""
    else:
        return functools.reduce(join, sentences[:n]) + "."
