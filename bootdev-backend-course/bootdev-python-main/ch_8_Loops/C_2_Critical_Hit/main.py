# code before changes:

# def calculate_flurry_crit(num_attacks, base_damage):
#     # ?

# assignment:

# In the calculate_flurry_crit function, 
# write a loop that calculates and returns the total_damage of the flurry as a critical hit.

# The function takes 2 inputs num_attacks, base_damage.

# Range over the num_attacks for the flurry

# Calculate the total damage for each attack within the flurry. 
# Remember, each attack is a critical hit and does double the base_damage!

# The final swing of the flurry should do 4x the base_damage
# Return the total damage

# actual code:

def calculate_flurry_crit(num_attacks, base_damage):
    all_damage = 0
    for i in range(1, (num_attacks+1)):
        if i == num_attacks:
            all_damage += (base_damage * 4)
        else:
           all_damage += (base_damage * 2)
    return all_damage



