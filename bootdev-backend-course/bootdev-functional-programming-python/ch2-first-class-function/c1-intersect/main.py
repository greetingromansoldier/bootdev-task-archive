# code before changes:

# def get_common_formats(formats1, formats2):
#     pass

# actual code:


def get_common_formats(formats1, formats2):
    return set(formats1).intersection(set(formats2))
