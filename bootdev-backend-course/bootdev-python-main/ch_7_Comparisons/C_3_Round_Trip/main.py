# code before changes:

# def has_enough_energy(energy_available, distance_one_way, meters_per_energy):
#     pass

# assignment:

# Complete the has_enough_energy function to check if Tyler can make a round trip. 
# The function takes 3 integers energy_available, distance_one_way, and meters_per_energy.

# Do some Pythonic math with the distance_one_way and meters_per_energy variables 
# to determine how many points of energy are needed for Tyler 
# to get to the capital city AND make it back to the inn.

# Assign the result to a energy_needed variable. 
# distance_one_way is how many meters it is to get from here to there. 
# meters_per_energy is how far Tyler's rogue can travel with one energy point.

# Return True if there is at least enough energy for a round trip 
# both there and back based on the energy_needed variable, and False otherwise.

# actual code:

def has_enough_energy(energy_available, distance_one_way, meters_per_energy):
    energy_needed = (distance_one_way * 2) / meters_per_energy
    if energy_available >= energy_needed:
        return True
    else:
        return False