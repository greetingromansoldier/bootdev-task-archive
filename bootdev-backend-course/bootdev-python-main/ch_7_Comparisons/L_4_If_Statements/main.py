# code before changes

# def print_status(player_health):
#     # ?

# assignment

# Complete the print_status function.

# If player_health is 0, print the text dead to the console.
# Afterwards, whether or not the player is dead, print the text status check complete to the console.

# actual code


def print_status(player_health):
    if player_health == 0:
        print("dead")
    print("status check complete")


# Don't edit below this line


def test(health):
    print(f"Player Health: {health}")
    print("Checking status...")
    print_status(health)
    print("=====================================")


def main():
    test(0)
    test(5)
    test(3)


main()