# code before changes:

# def get_last_index(inventory):
#     pass

# assignment:

# Some of our player's inventories are huge, so looking through the entire list is cumbersome. 
# Let's find an easy way for us to get the index of the last item in their inventory.

# Complete the get_last_index function so that it returns the length of the inventory list minus 1.

# actual code:

def get_last_index(inventory):
    get_last_index = len(inventory) - 1
    return get_last_index