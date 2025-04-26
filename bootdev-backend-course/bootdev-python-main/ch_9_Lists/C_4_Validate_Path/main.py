# code before changes:

# def validate_path(expected_path, character_path):
#     pass

# assignment:

# Complete the validate_path function. 
# It should compare the expected sequence of waypoints with 
# the actual sequence taken by a character and calculate 
# how accurately the character followed the intended path.

# INPUT

# 1) expected_path: A list of waypoints that define the correct path for the quest.
# 2) character_path: A list where the first index is the name of the character, 
# and the rest of the list consists of the waypoints they actually visited.

# character_path contains the same number of waypoints as expected_path.


# OUTPUT

# The function should return 2 values:

# 1) character_name: a string
# 2) percentage: a float

# EXAMPLE

# expected_path = ["A", "B", "C", "D"]
# character_path = ["Hero123", "A", "C", "B", "D"]
# name, percent = validate_path(expected_path, character_path)
# print(name, percent)
# # prints: Hero123, 50.0


# actual code:

# plan:

# 1) comparing

def validate_path(expected_path, character_path):
    character_name = character_path.pop(0)
    counter = 0
    for i in range(0, len(expected_path)):
        if expected_path[i] == character_path[i]:
            counter += 1

    percentage = (counter / len(expected_path)) * 100

    return character_name, percentage


# такой вариант мне нравится больше чем в прошлом задании. он как-то гораздо проще и понятнее
# ноооо походу прошлое задание таким образом выполнить не получится (Alchemy Ingredients) потому что
# в этом случае нам важен порядок элементов, а в том нет, там мы каждый раз проверяем весь список на элемент

