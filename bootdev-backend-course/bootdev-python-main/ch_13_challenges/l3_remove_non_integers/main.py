# code before changes:

# def remove_nonints(nums):
#     pass

# assignment:

# Complete the remove_nonints() function that takes a list and returns
# a new list with all the non-integer types removed.

# remove_nonints(["1", 1, "3", "400", 4, 500])
# # Remaining list after removing nonints = [1, 4, 500]

# You can check a variable's type using the type() function.

# if type(variable) == int:

# Do not change the input nums list, return a new list with only the integers.

# actual code:

def remove_nonints(nums):
    only_ints = []
    for num in nums:
        if type(num) == int:
            only_ints.append(num)
    return only_ints