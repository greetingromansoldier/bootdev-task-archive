# code before changes

# def max_players_on_server():
#     pass

# task

# Due to the constraints of our app's server, there is a maximum number of 
# players we can have on a single Fantasy Quest server.

# Complete the max_players_on_server function. 
# It takes no inputs, but simply returns 3 static numbers:

# The max players on a "small" server: 1,024,000,000,000,000,000 (1.024e18)
# The max players on a "medium" server: 10,240,000,000,000,000,000
# The max players on a "large" server: 102,400,000,000,000,000,000


def max_players_on_server():
    small = 1.024e18
    medium = 10.240e18
    large = 102.4e18
    return small, medium, large

