# code before changes:

#     for i in range(0, len(items)):
#         pass

# assignment:

# Our players need a way to see how many copies of a specific item they have within their inventory!

# Let's finish the get_item_counts function. 
# Within the loop, check if the items are a Potion, Bread, or Shortsword, 
# then add up how many there are of each by incrementing the potion_count, 
# bread_count and shortsword_count variables respectively.

# actual code:

def get_item_counts(items):
    potion_count = 0
    bread_count = 0
    shortsword_count = 0

    # don't touch above this line

    for i in range(0, len(items)):
        if items[i] ==  'Potion':
            potion_count += 1
            print(f"potion_count: {potion_count}")
        elif items[i] == "Bread":
            bread_count += 1
            print(f"bread_count: {bread_count}")
        elif items[i] == "Shortsword":
            shortsword_count += 1
            

    # don't touch below this line

    return potion_count, bread_count, shortsword_count