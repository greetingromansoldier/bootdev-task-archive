# code before changes:

# def remove_invalid_lines(document):
#     pass

# actual code:

# remove lines with * +
# preserve trailing newlines
# return new document list


def remove_invalid_lines(document):
    return "\n".join(filter(lambda line: not line.startswith("-"), document.split("\n")))
