# code before changes:

# def find_min(nums):
#     pass

# assignment:

# Write a function called find_min() that finds the smallest number in a list

# find_min([1, 3, -1, 2]) -> -1

# find_min([18, 3, 7, 2]) -> 2

# (use biult-in infinity)

# actual code:

def find_min(nums):
    min_num = float("inf")
    for num in nums:
        if num < min_num:
            min_num = num
    return min_num