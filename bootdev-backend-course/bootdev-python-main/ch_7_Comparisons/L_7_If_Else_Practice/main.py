# code before changes:

# def check_high_score(current_player_name, high_scoring_player_name):
#     if True:
#         return "You are the highest scoring player!"
#     else:
#         return "You are not the highest scoring player!"
    
# assignment:

# There is a bug in the check_high_score function! 
# Add the proper conditional statement to fix the bug. 

# If the names match, return the string:
# You are the highest scoring player!

# Otherwise, return:
# You are not the highest scoring player!


# code after changes:

def check_high_score(current_player_name, high_scoring_player_name):
    if current_player_name == high_scoring_player_name:
        return "You are the highest scoring player!"
    else:
        return "You are not the highest scoring player!"