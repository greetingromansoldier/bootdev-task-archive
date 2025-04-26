# code before changes:

# def generate_user_list(num_of_users):
#     player_ids = []

#     for i in range(0, num_of_users):
#         pass

#     return player_ids

# assignment:

# We need to generate a unique user ID for each player in the game. 
# An ID is just a unique number that identifies a user.

# Let's finish the generate_user_list function. 
# In the body of the loop, use the incrementing value i as unique IDs and append them to the player_ids list.

# actual code:

def generate_user_list(num_of_users):
    player_ids = []

    for i in range(0, num_of_users):
        player_ids.append(i)
        i += 1

    return player_ids