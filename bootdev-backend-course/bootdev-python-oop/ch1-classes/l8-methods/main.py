# code before changes
#
# class Wall:
#     armor = 10
#     height = 5

#     def fortify(self):
#         pass

# assignment:

# Add a fortify() method to your wall class. It should double the current armor property.

# actual code:

class Wall:
    armor = 10
    height = 5

    def fortify(self):
        self.armor *= 2
        return self.armor
