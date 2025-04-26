# code before changes:

# def get_median_font_size(font_sizes):
#     pass

# actual code:

def get_median_font_size(font_sizes):
    sort_font_sizes = sorted(font_sizes)
    middle_index = len(sort_font_sizes) // 2

    if len(font_sizes) == 0:
        return None
    elif (len(font_sizes) % 2) != 0:
        return sort_font_sizes[middle_index]
    else:
        return sort_font_sizes[middle_index-1]

# gemini says my code is good according to assignment but actual solution from the course is:

# def get_median_font_size(font_sizes):
    # if len(font_sizes) == 0:
    #     return None
    # return sorted(font_sizes)[(len(font_sizes) - 1) // 2]
