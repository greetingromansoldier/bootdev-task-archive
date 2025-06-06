# code before changes:

# class Sword:
#     def __init__(self, sword_type):
#         self.sword_type = sword_type

#     def __add__(self, other):
#         pass


# actual code:

class Sword:
    def __init__(self, sword_type):
        self.sword_type = sword_type

    def __add__(self, other):
        if self.sword_type == "bronze" and other.sword_type == "bronze":
            return Sword("iron")
        if self.sword_type == "iron" and other.sword_type == "iron":
            return Sword("steel")

        raise Exception("cannot craft")
