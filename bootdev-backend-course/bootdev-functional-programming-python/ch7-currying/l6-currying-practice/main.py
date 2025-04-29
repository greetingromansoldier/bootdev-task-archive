# code before changes:

# def new_resizer(max_width, max_height):
#     pass

# actual code:

def new_resizer(max_width, max_height):

    def inner_function (min_width=0, min_height=0):
        if min_width > max_width or min_height > max_height:
            raise Exception("minimum size cannot exceed maximum size")

        def innermost_function (width, height):
            if width < min_width:
                width = min_width
            if width > max_width:
                width = max_width

            if height < min_height:
                height = min_height
            if height > max_height:
                height = max_height
            return width, height

        return innermost_function

    return inner_function

# here's the author's solution for intermost_function(), how to keep height and width in some boundaries:

        # new_width = max(min_width, min(width, max_width))
        # new_height = max(min_height, min(height, max_height))

# I thought my way here and I think in some way it is.... more readable
