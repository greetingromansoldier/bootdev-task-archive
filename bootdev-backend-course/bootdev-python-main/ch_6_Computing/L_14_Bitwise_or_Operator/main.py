# code before changes

# def calculate_guild_perms(glorfindel, galadriel, elendil, elrond):
#     pass

# task

# Complete the calculate_guild_perms function. It takes as input 
# four binary numbers representing the separate permissions of each member of the guild: 
# glorfindel, galadriel, elendil and elrond. 
# It should return a single binary number that represents the combined permissions of all the members of the guild.

# Use a series of bitwise "or" operations to calculate the superset of all the member's permissions.

def calculate_guild_perms(glorfindel, galadriel, elendil, elrond):
    superset = glorfindel | galadriel | elendil | elrond
    return superset

