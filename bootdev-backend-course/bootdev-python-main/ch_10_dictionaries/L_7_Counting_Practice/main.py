# code before changes:

# def count_enemies(enemy_names):
#     enemies_dict = {}
#     for enemy_name in enemy_names:
#         enemies_dict[enemy_name] += 1
#     return enemies_dict

# assignment:

# We need to be able to report to our players how many enemies are in their immediate vicinity - 
# but they want the count of each enemy by its kind. 

# Fix the count_enemies function. 

# 1) If you run the code, it will result in a KeyError. 
# 2) It takes a list of enemy_names as input. 
# 3) It should return a dictionary where the keys are all the enemy names from the list, 
# 4) and the values are the counts of how many times each enemy appeared in the list.

# actual code:

def count_enemies(enemy_names):
    enemies_dict = {}
    for enemy_name in enemy_names:
        checker = enemy_name in enemies_dict
        if checker == True:
            enemies_dict[enemy_name] += 1
        else:
            enemies_dict[enemy_name] = 1
    return enemies_dict

