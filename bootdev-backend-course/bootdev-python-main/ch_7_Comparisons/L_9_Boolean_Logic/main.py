# code before changes:

# def does_attack_hit(attack_roll, armor_class):
#     pass

# assignment:

# We need a way for our game to track whether a character's attack hits or misses.

# Complete the does_attack_hit function. 
# The function should return True if either of the following conditions are met:

# - The attack_roll is not a 1 and the attack roll is greater than or equal to the armor_class, or
# - The attack roll is a 20
# Otherwise, it should return False.

# actual code:

def does_attack_hit(attack_roll, armor_class):
    if (attack_roll != 1 and attack_roll >= armor_class) or attack_roll == 20:
        return True
    else:
        return False
