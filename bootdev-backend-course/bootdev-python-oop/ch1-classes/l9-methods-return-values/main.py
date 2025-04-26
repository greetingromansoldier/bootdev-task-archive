# code before changes
# class Wall:
#     armor = 10
#     height = 5

#     def get_cost(self):
#         pass

#     # don't touch below this line

#     def fortify(self):
#         self.armor *= 2

# assignment

# Add a .get_cost() method to your Wall class.
# What do you think it should return? The cost of a wall is the product of its height and armor:

# cost = armor * height


# actual code


class Wall:
    armor = 10
    height = 5

    def get_cost(self):
        cost = self.armor * self.height
        return cost

    # don't touch below this line

    def fortify(self):
        self.armor *= 2
