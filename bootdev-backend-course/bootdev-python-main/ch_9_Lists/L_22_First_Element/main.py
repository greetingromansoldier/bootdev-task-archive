# code before changes:

# def get_first_item(items):
#     pass

# assignment:

# Let's add another function to our inventory system. 

# Write a function that returns the first element from a list. 
# If the list is empty then return the string ERROR instead.

# actual code:

def get_first_item(items):
    if len(items) == 0:
        return "ERROR"
    else:
        return items[0]
    

# задание показалось довольно сложным сначала)

        