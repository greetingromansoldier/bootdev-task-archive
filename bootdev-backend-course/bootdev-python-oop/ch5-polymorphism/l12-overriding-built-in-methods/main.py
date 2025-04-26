# code before changes:

# class Dragon:
#     def __init__(self, name, color):
#         self.name = name
#         self.color = color

#     def __str__(self):
#         pass

# actual code:

class Dragon:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def __str__(self):
        return f"I am {self.name}, the {self.color} dragon"
