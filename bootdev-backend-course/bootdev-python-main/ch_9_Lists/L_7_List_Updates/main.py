# code before changes:

# def smelt_ore(inventory):
#     # ?

#     return inventory

# assignment:

# Fantasy Quest is trialing a new inventory system for their hardcore game mode.
# If a player has Iron Ore or an Iron Bar,  it is always stored in the 2nd inventory slot
# (and they can only have one or the other).

# Let's finish the smelt_ore function. 
# When a player tries to smelt Iron Ore we need to change it into an Iron Bar, 
# but only if they already have Iron Ore in their inventory slot.

# actual code:

def smelt_ore(inventory):
    if inventory[1] == "Iron Ore":
        inventory[1] = "Iron Bar"
    else:
        None

    return inventory