# code before changes:

# def meditate(mana, max_mana, energy, energy_drinks):
#     pass

# assignment:

# Complete the meditate function using a while loop. It takes mana, max_mana, energy and energy_drinks integers.

# - While meditating, a character converts 1 energy into 1 mana for each iteration of the loop, up to the max_mana.
    
# - If they have any energy_drinks when they run out of energy, 
#   they will drink 1 energy potion to gain 50 energy and continue meditating.

# - A character will stop meditating if either:
#   - Their mana reaches the max_mana, or
#   - They run out of both energy and energy_drinks.

# Return the mana and remaining energy and energy_drinks when the character stops meditating.

# actual code:

def meditate(mana, max_mana, energy, energy_drinks):
    while mana < max_mana and  (energy > 0 or energy_drinks > 0):
        if energy < 1 and energy_drinks > 0:
            energy_drinks -= 1
            energy += 50
        else:
            energy -= 1
            mana += 1
    return mana, energy, energy_drinks

# бля ну тоже методом тыка по сути, просто разруливал возникшие баги хз, 
# не то шобы внутрянку полностью понял