# code before changes:

# def add_format(default_formats, new_format):
#     default_formats[new_format] = True
#     return default_formats


# def remove_format(default_formats, old_format):
#     default_formats[old_format] = False
#     return default_formats

# actual code:

def add_format(default_formats, new_format):
    new_formats = default_formats.copy()
    new_formats[new_format] = True
    return new_formats


def remove_format(default_formats, old_format):
    new_formats = default_formats.copy()
    new_formats[old_format] = False
    return new_formats
