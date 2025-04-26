# code before changes:

# def calculate_experience_points(level):
#     pass

# task text:

# You've been hired by a game studio to work on their latest role-playing game. 
# In this game adventurers need experience points (XP) to level up and become stronger.
# You've been tasked with updating a part of the player statistics panel. 
# We want to show the total xp a player has gained based on their current level.

# Each character starts with 0 XP at level 1. 
# To reach the next level, they need XP equal to their current level times 5.

# Level	XP      To Next Level	    Total XP Gained
# 1	            5	                0
# 2	            10	                5
# 3	            15	                15
# 4	            20	                30


# assignment:

# Complete the calculate_experience_points function.

# The calculate_experience_points function takes a single parameter named level. 
# Determine the total XP they have gained to reach the specified level from level 1 and return it.

# actual code:

def calculate_experience_points(level):
    xp = 0
    for i in range(1, level):
        xp += i * 5
        print(f"level: {i}, xp: {xp}")
    return xp