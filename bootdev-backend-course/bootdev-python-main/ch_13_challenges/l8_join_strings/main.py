# code before changes:

# def join_strings(strings):
#     pass

# assignment:

# Write a function called join_strings() that takes a list of strings and returns a single string. 
# Concatenate the strings from the list end-to-end, in order, with a comma between them. 
# Don't use the .join() string method.

# Example:

# string_list = ["hello", "my", "friend"]
# joined_string = join_strings(string_list)
# print(joined_string) # "hello,my,friend"


# Tip

# You don't want a comma at the beginning or the end of the final string!


# actual code:

def join_strings(strings):
    joined_string = "" 
    comma_index = len(strings)-1
    for i in range(0, len(strings)):
        joined_string += strings[i]
        if i < comma_index:
            joined_string += ","
    return joined_string 