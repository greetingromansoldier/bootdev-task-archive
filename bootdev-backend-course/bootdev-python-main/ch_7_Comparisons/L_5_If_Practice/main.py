# code before changes

# def check_swords_for_army(number_of_swords, number_of_soldiers):
#     pass

# assignment

# Complete the check_swords_for_army function. 

# If the number of swords and the number of soldiers match, return the string:
# correct amount

# Otherwise, return the string:
# incorrect amount

# Punctuation matters! Make sure you return the strings exactly as they appear above.

# actual code

def check_swords_for_army(number_of_swords, number_of_soldiers):
    if number_of_soldiers == number_of_swords:
        return 'correct amount'
    else:
        return 'incorrect amount'