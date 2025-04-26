# code before changes:

# def merge(dict1, dict2):
#     pass


# def total_score(score_dict):
#     pass

# assignment:

# Complete the merge and total_score functions.

# 1) merge

# Complete the merge function. 
# It accepts two score dictionaries as input and returns a single merged dictionary that contains 
# all of the keys and values from the input dictionaries.

# If a key exists in both dictionaries, the value from the second dictionary should overwrite the value from the first dictionary. 
# Here is an example of how the merge function should execute when implemented correctly:

# two_towers = {"Frodo": "One Ring", "Aragorn": "Narsil"}
# rotk = {"Aragorn": "Andúril", "Gandalf": "Glamdring"}
# merged_dict = merge(two_towers, rotk)
# print(merged_dict)
# # {'Frodo': 'One Ring', 'Aragorn': 'Andúril', 'Gandalf': 'Glamdring'}

# 2) total_score

# This function should take a single score dictionary as input and return the total score calculated from the values of that dictionary.

# If no points were scored, the function should return 0.

# Don't forget: you can always add print() statements to your code so that you can debug your code before submitting! 
# Print out values of variables to see what's going on, and question your assumptions about what you think is happening.

# Example of Debugging With Print Statements:

# def total_score(score_dict):
#     print(f"score_dict: {score_dict}")
#     for key in score_dict:
#         print(f"key: {key}")

# You would then run your code and manually inspect the output to see what's going on. 
# You can always remove the print statements when you're done debugging if you want.

# actual code:

def merge(dict1, dict2):
    score_dict = {}
    for key in dict1:
        value = dict1[key]
        score_dict[key] = value
    


    for key in dict2:
        value = dict2[key]
        score_dict[key] = value
    
    return score_dict
    



def total_score(score_dict):
    total_score = 0
    if score_dict != None:
        for key  in score_dict:
            total_score += score_dict[key]
    else: 
            return None
    
    return total_score