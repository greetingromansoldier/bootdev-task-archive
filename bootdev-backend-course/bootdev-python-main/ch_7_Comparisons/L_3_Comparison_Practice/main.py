# code before changes

# def can_withstand_blow(hero_armor, enemy_damage):
#     pass

# assignment

# Complete the can_withstand_blow function. 
# It should return True if the hero's armor is greater than or equal 
# to the damage dealt by the enemy, and False otherwise.

# actual code

def can_withstand_blow(hero_armor, enemy_damage):
    if hero_armor >=enemy_damage:
        return True
    else:
        return False