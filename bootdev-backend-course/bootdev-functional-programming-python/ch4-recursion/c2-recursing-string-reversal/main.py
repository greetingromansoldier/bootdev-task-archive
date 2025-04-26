# code before changes:

# def reverse_string(s):
#     pass

# actual code:

# solve a small problem
#   - take 1 symbol from the end and add to the front
# call a recursion
# base case

# first char is string[0]
# others are string[1:]

def reverse_string(s):
    new_string = ""
    if len(s) > 0:
        new_string += s[-1]
        s = s[:-1]
        result = reverse_string(s)
        new_string += result
        return new_string
    else:
        return ""
