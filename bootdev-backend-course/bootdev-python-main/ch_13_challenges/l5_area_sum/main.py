# code before changes:

# def area_sum(rectangles):
#     pass

# assignment:

# Complete the area_sum() function. 
# It accepts a list of rectangles, where each rectangle is a dictionary that has the following structure:

# {
#   "height": 5,
#   "width": 6
# }

# The function will calculate the area of each rectangle, then sum them all up and return the result.

# actual code:

def area_sum(rectangles):
    rectangles_sum = 0
    area = 0
    for rectangle in rectangles:
        area = rectangle["height"] * rectangle["width"]
        rectangles_sum += area
    
    return rectangles_sum