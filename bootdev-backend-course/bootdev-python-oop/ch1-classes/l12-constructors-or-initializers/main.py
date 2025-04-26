# code before changes:

# class Wall:
#     def __init__(self, depth, height, width):
#         pass

# assignment:

# Add a constructor to our Wall class.

#1) It should take depth, height and width as parameters, in that order, and set them as properties.
#2) Compute an additional property called volume. Volume is the depth times height times width.


# actual code:

class Wall:
    def __init__(self, depth, height, width):
        self.depth = depth
        self.height = height
        self.width = width
        self.volume = self.depth * self.height * self.width
