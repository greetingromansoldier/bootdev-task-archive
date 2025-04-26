# code before changes

# def binary_string_to_int(num_servers, num_players, num_admins):
#     pass

# task

# Complete the binary_string_to_int function. It takes three binary strings as input and returns each of them in the same order as integers. Each integer is the numerical value of the string when interpreted as binary.

# For example:

# data_a, data_b, data_c = binary_string_to_int("100", "101", "110")
# print(data_a)
# # 4
# print(data_b)
# # 5
# print(data_c)
# # 6

def binary_string_to_int(num_servers, num_players, num_admins):
    num_servers, num_players, num_admins = int(num_servers, 2), int(num_players, 2), int(num_admins, 2)
    return num_servers, num_players, num_admins