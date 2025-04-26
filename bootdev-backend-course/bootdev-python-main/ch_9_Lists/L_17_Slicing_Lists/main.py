# code before changes:

# def get_champion_slices(champions):
#     pass

# assignment:

# Complete the given get_champion_slices function. 
# It takes a list of champions and should return three new lists based on the given champions:

# First, return a slice of the champions list that starts with the third champion and goes to the end of the list.

# Next, return a slice of the champions list that starts at the beginning of the list and ends 
# with the third champion from the end (inclusive).

# Last, return a slice of the champions list that only includes the champions in even numbered indexes.

# actual code:

def get_champion_slices(champions):
    first_slice = champions[2:]
    second_slice = champions[:-2]
    third_slice = champions[::2]
    return first_slice, second_slice, third_slice