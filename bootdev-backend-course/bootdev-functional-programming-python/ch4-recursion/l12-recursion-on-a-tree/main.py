# code before changes:

# def list_files(parent_directory, current_filepath=""):
#     pass

# actual code:

def list_files(parent_directory, current_filepath=""):
    paths = []
    for key in parent_directory:
        new_filepath = current_filepath + "/" + key
        if parent_directory[key] == None:
            paths.append(new_filepath)
        else:
            inside_paths = list_files(parent_directory[key], new_filepath)
            paths.extend(inside_paths)


    return paths
