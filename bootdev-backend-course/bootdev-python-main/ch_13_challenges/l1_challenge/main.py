# code before changes:

# def number_sum(n):
#     pass

# assignment:

# Write a function called number_sum(n) that adds up all the numbers from 1 to n. For example:

# number_sum(5) -> 1+2+3+4+5 -> 15

# number_sum(3) -> 1+2+3 -> 6

# actual code:

def number_sum(n):
    a = 0
    for i in range(0, n+1):
        a += i

    return a

print(number_sum(5))