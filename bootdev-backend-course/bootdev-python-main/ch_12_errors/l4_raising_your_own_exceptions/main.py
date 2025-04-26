# code before changes:

# def get_player_record(player_id):
#     if player_id == 1:
#         return {"name": "Slayer", "level": 128}
#     if player_id == 2:
#         return {"name": "Dorgoth", "level": 300}
#     if player_id == 3:
#         return {"name": "Saruman", "level": 4000}
#     pass

# assignment:

# If a player_id that doesn't exist is passed into the get_player_record function, 
# we need to raise (but not handle) our own error to alert the caller of our function that the player they are looking for doesn't exist. 
# The exception should say player id not found.

# Note: the tests will call the get_player_record function, and will handle the exception you raise.

# actual code:

def get_player_record(player_id):
        if player_id == 1:
            return {"name": "Slayer", "level": 128}
        if player_id == 2:
            return {"name": "Dorgoth", "level": 300}
        if player_id == 3:
            return {"name": "Saruman", "level": 4000}
        raise Exception("player id not found")