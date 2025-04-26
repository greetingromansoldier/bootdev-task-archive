# code before changes:

# def deduplicate_lists(lst1, lst2, reverse=False):
#     pass

# actual code:

def deduplicate_lists(lst1, lst2, reverse=False):
    if reverse == True:
        return sorted(set(lst1 + lst2), reverse=True)
    else:
        return sorted(set(lst1 + lst2), reverse=False)
