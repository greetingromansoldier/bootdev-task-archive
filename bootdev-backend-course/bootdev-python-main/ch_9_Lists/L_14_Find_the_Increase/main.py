# code before changes:

#     for i in range(0, len(old_character_levels)):
#         # ?

# assignment:

# We keep track of each character's level in a list. 
# When someone levels up, we want to know about it so we can congratulate them! 

# Your assignment is to compare the old_character_levels and new_character_levels lists and to print the index 
# where a character's level increased.

# The existing code in the loop you've been given loops over all of the indexes in old_character_levels. 
# Because old_character_levels and new_character_levels are the same lengths, you can reuse i to index into both.

# Fill in the loop with code that prints the indexes where the item in the first list is less than the item in the second list; 
# we don't want to congratulate someone for staying the same level (or somehow leveling down). For example, if the lists are:

# old_character_levels = [2, 5, 3, 7, 5]
# new_character_levels = [2, 5, 19, 7, 8]

# Then your code should print these indexes:
# 2
# 4

# actual code:


def check_character_levels():
    old_character_levels = [1, 42, 43, 53, 12, 3, 32, 34, 54, 32, 43]
    new_character_levels = [1, 42, 45, 54, 12, 3, 32, 38, 54, 32, 42]

    # don't touch above this line

    for i in range(0, len(old_character_levels)):
        if old_character_levels[i] < new_character_levels[i]:
            print(i)


# don't touch below this line


def test():
    print("Character level increased at indexes:")
    check_character_levels()
    print("=====================================")


def main():
    test()


main()