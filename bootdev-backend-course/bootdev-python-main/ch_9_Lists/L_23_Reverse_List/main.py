# code before changes:

# def reverse_array(items):
#     pass

# assignment:

# Some of our players would like to view their inventories in reverse order.

# Let's write a function that takes a list as an input and returns a new list except all the items are in reverse order.

# For example:

# [1, 2, 3] -> [3, 2, 1]
# ['a', 'b', 'c', 'd'] -> ['d', 'c', 'b', 'a']

# actual code:

def reverse_array(items):
    reverse_items = []
    while len(items) > 0:
        cached_item = items.pop()
        reverse_items.append(cached_item)
    
    return reverse_items

# тоже интересная, но немного сложная и запутанная таска

