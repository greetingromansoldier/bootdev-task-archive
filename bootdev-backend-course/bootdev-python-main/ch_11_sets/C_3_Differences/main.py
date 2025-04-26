# code before changes:

# def find_missing_ids(first_ids, second_ids):
#     pass

# assignment:

# Complete the find_missing_ids function. 
# It accepts two lists as input, and returns a new list of all the IDs present in the first list but not the second. 
# Make sure to remove any duplicates.

# actual code:

def find_missing_ids(first_ids, second_ids):
    first_ids_set = set(first_ids)
    second_ids_set = set(second_ids)
    only_first_ids = first_ids_set - second_ids_set
    only_first_ids = list(only_first_ids)
    return only_first_ids