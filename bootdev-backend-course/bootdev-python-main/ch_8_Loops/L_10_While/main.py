# code before changes:

# def regenerate(current_health, max_health, enemy_distance):
#     pass

# assignment:

# In Fantasy Quest, player characters regenerate health when standing still while away from enemies. 
# This means they will gain health but can't run from enemies that are coming towards them while regenerating.

# Complete the regenerate function using a while loop. It takes current_health, max_health and enemy_distance integers.

# While regenerating health, a character gains 1 health each iteration until it reaches the max_health amount.
# The enemy_distance shortens by 2 for each iteration.
# If an enemy is at a distance of 3 or less from the character, the character stops gaining health.
# Return the new current_health after health regeneration stops.

# actual code:

def regenerate(current_health, max_health, enemy_distance):
    while enemy_distance > 3:
        if current_health < max_health:
            current_health += 1  
            enemy_distance -= 2
        else:
            break
    return current_health
    
# тяжёленькая хуйня для меня была эти while loops бля