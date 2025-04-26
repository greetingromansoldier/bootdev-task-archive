# code before changes:

# def split_players_into_teams(players):
#     pass

# assignment:

# Complete the split_players_into_teams function. Use a slice with a "step" to create two new lists from the players list:

# even_team should have the players with even-numbered indexes.
# odd_team should have the players with odd-numbered indexes.
# Return even_team and odd_team in that order. Be careful not to assign the wrong values to these variables!


# actual code:

def split_players_into_teams(players):
    even_team = players[::2]
    odd_team = players[1::2]
    return even_team, odd_team