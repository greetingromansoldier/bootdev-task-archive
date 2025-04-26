# code before changes

# def main():
#     calculate_dps(8, 000, 000, 45)
#     calculate_dps(10, 000, 000, 49)


# # Don't edit below this line


# def calculate_dps(damage, time):
#     dps = damage / time
#     print(f"Damage per second: {dps}")
#     print("=====================================")


# main()

# task

# Fix the intern's syntax error. 
# The calculate_dps function takes two inputs, but due to the syntax error, 
# it's taking in 4 instead. Use the proper delimiter so that the numbers are still easy to parse visually.

# The two input numbers should be:

# damage: 8 million, time: 45
# damage: 10 million, time: 49

def main():
    calculate_dps(8_000_000, 45)
    calculate_dps(10_000_000, 49)


# Don't edit below this line


def calculate_dps(damage, time):
    dps = damage / time
    print(f"Damage per second: {dps}")
    print("=====================================")


main()