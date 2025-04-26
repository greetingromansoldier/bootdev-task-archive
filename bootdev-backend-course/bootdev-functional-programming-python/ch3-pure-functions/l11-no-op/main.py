# code before changes:

# def remove_emphasis_from_word(word):
#     # ?


# def remove_emphasis_from_line(line):
#     # ?


# def remove_emphasis(doc_content):
#     # ?

# actual code:

def remove_emphasis_from_word(word):
    return word.strip("*")


def remove_emphasis_from_line(line):
    return " ".join(map(remove_emphasis_from_word, line.split(" ")))


def remove_emphasis(doc_content):
    return "\n".join(map(remove_emphasis_from_line, doc_content.split("\n")))

# it was pretty hard tbh
