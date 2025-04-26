# code without changes

def destroy_wall(wall_health):
    for w in wall_health:
        if w <= 0:
            wall_health.remove(w)
    return wall_health

# assignment 

# The test suite expects a different function name. 
# Take a look at the main_test.py file to see what it's looking for, 
# and rename the function accordingly.

# actual code
def destroy_walls(wall_health):
    for w in wall_health:
        if w <= 0:
            wall_health.remove(w)
    return wall_health
