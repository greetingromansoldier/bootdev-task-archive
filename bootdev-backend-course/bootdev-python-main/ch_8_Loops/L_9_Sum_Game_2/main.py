# code before changes:

# def sum_of_odd_numbers(end):
#     total = 0
#     for i in range(0, end):
#         total += i
#     return total

# assignment:

# Complete the sum_of_odd_numbers function. 
# It should calculate the sum of all the odd numbers 
# starting at 1 up to (but not including) the given end number and return the result.

# actual code:

def sum_of_odd_numbers(end):
    total = 0
    for i in range(1, end, 2):
        total += i
    return total

