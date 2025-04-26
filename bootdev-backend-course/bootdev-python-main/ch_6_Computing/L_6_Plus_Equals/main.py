# code before changes

# def get_hurt(current_health, damage):
#     pass

# task

# Complete the get_hurt function. It should use the -= 
# in-place operator to subtract damage from current_health and then return the new current_health.

# Note: You cannot use -= in a return statement. Set the variable first, and then return it after!



def get_hurt(current_health, damage):
    current_health -= damage
    return current_health