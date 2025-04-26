# code before changes:

# def remove_duplicates(lst):
#     pass

# assignment:

# Complete the remove_duplicates function. 
# It accepts a list of strings and removes any duplicate values. 
# It should utilize and return a set, not a list!

# Bonus points if you can write the body of the function in a single line of code.

# actual code:

def remove_duplicates(lst):
    set_from_lst = set(lst)
    return set_from_lst