# code without changes

def fight_soldiers(soldier_one, soldier_two):
    soldier_one_dps = soldier_one["damage"] * soldier_one["attacks_per_second"]
    soldier_two_dps = soldier_two["damage"] * soldier_two["attacks_per_second"]
    if soldier_one_dps > soldier_two_dps:
        return "soldier 1 wins"
    if soldier_two_dps > soldier_one_dps:
        return "soldier 2 wins"
    return "both soldiers die"

# assignment

# Your manager noticed that there's a lot of repetitive code in the "Age of Dragons" code base.
# She asked you to update the fight_soldiers function so that the DPS
# (damage-per-second) calculation is only written once.

# Notice how these two lines are practically identical:

# soldier_one_dps = soldier_one["damage"] * soldier_one["attacks_per_second"]
# soldier_two_dps = soldier_two["damage"] * soldier_two["attacks_per_second"]

# Create a new function called get_soldier_dps that takes a soldier
# and returns its DPS using the same logic as the lines above.

# Replace the two lines above with calls to get_soldier_dps.

# actual code

def fight_soldiers(soldier_one, soldier_two):

    # soldier_one_dps = soldier_one["damage"] * soldier_one["attacks_per_second"]
    # soldier_two_dps = soldier_two["damage"] * soldier_two["attacks_per_second"]
    if get_soldier_dps(soldier_one) > get_soldier_dps(soldier_two):
        return "soldier 1 wins"
    if get_soldier_dps(soldier_two) > get_soldier_dps(soldier_one):
        return "soldier 2 wins"
    return "both soldiers die"

def get_soldier_dps(soldier_stats):
    soldier_dps = soldier_stats["damage"] * soldier_stats["attacks_per_second"]
    return soldier_dps
