# code before changes:

# def get_most_common_enemy(enemies_dict):
#     pass

# assignment:

# We need to display on our player's screens what the most common enemy in a given area of the game map is.

# Complete the get_most_common_enemy function by iterating over all enemies in the dictionary 
# and returning only the name of the enemy with the highest count.

# If there are no enemies, return None. If there are multiple enemies with the same highest count, return the first one found.

# enemies_dict is a dictionary of name -> count. Example:

# {
#     "jackal": 1,
#     "kobold": 2,
#     "soldier": 3,
#     "gremlin": 5
# }

# actual code:

def get_most_common_enemy(enemies_dict):
    most_common_enemy_counter = float("-inf")
    most_common_enemy = None
    for enemy in enemies_dict:
        if enemies_dict[enemy] > most_common_enemy_counter:
            most_common_enemy = enemy
            most_common_enemy_counter = enemies_dict[enemy]
        elif enemies_dict[enemy] == most_common_enemy_counter:
            continue
        elif enemies_dict[enemy] < most_common_enemy_counter:
            continue
        else:
            return None
        
    return most_common_enemy
