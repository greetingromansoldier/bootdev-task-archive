# code before changes:

# def is_prime(number):
#     pass

# assignment:

# The team wants the random events to trigger on prime numbers. 
# Write a function that takes a single number as input and returns True if it is a prime number or False if it is not.

# prime number - is a positive integer, greater than 1, that is only divisible by itself and 1.
# 0 and 1 are not prime numbers!
# And don't forget to catch all negative numbers!

# actual code:

def is_prime(number):
    even = number % 2
    odd = number % 3
    if number >  1:
        if number != 2 and even != 0 and number != 3 and odd != 0:
            print("here 1")
            return True
        elif number != 2 and even == 0 or number != 3 and odd == 0:
            print("here 2")
            return False
        elif number ==  2:
            print("here 3")
            return True
    else:
        return False

# тоже тяжёлая хуета была, тупо методом проб и ошибок сделал
