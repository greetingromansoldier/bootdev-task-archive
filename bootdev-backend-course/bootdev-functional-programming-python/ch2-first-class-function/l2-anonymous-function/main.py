# code before changes:

# def file_type_getter(file_extension_tuples):
#     pass

# actual code:

def file_type_getter(file_extension_tuples):

    extension_dict = {}
    for item in file_extension_tuples:
        for i in range(0, len(item[1])):
            extension_dict[item[1][i]] = item[0]

    get_extension = lambda string: extension_dict.get(string, "Unknown")
    return get_extension
