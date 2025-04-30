# code before changes:

# def markdown_to_text_decorator(func):
#     def wrapper(*args, **kwargs):
#         pass
#
#     return wrapper

# actual code:

def markdown_to_text_decorator(func):
    def wrapper(*args, **kwargs):

        def transformation_helper (tuple_input):
            key, value = tuple_input
            return (key, convert_md_to_txt(value))

        new_list = list(map(convert_md_to_txt, args))

        dict_items = kwargs.items()
        dict_out = dict(map(transformation_helper, dict_items))

        return func(*new_list, **dict_out)

    return wrapper


# don't touch below this line


def convert_md_to_txt(doc):
    lines = doc.split("\n")
    for i in range(len(lines)):
        line = lines[i]
        lines[i] = line.lstrip("# ")
    return "\n".join(lines)
