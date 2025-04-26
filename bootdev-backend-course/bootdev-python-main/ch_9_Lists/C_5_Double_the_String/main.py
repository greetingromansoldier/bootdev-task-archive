# code before changes:

# def double_string(string):

#     pass

# assignment:

# The fantasy quest team wants to add a new easter egg potion to Fantasy Quest! 
# It causes characters to have their in-game chat manipulated when they send messages. 
# The potion doubles every character they send!

#     The message they type: Hello there
#     The message that is sent: HHeelllloo  tthheerree

# Complete the double_string function. It takes a string as input and returns a "doubled" version, including spaces!

# Example output:

# sentence = "LF3M BRD full clear"
# print(double_string(sentence)) # "LLFF33MM  BBRRDD  ffuullll  cclleeaarr"

# actual code:

# plan:
# 1) make a list with characters from the input string using strip() method
# 2) double every character (I think by changing the value in this very list)
# 3) 

def double_string(string):
    double_string = []
    for character in string:
        character *= 2
        double_string.append(character)

    double_string = "".join(double_string)

    return double_string