# code before changes:

# class Dragon:
#     element = "ice"

#     def __init__(self, element):
#         return

#     def get_breath_damage(self):
#         if self.element == "fire":
#             return 300
#         if self.element == "ice":
#             return 150
#         return 0

# assignment:

#Some lazy code that's managed by another development team is causing some bugs in our team's class.
#We can fix it by using instance variables instead of class variables.

#In the main() function (that our team isn't responsible for),
#a line like Dragon.element = "fire" should not affect our existing dragon instances!

#We want our users to specify each dragon's element type when they create a new dragon with the constructor.

#Update the Dragon class.

#1) Remove the element class variable.
#2) Use an instance variable for element that's configurable via the constructor.

# actual code:

class Dragon:
    def __init__(self, element):
        self.element = element

    def get_breath_damage(self):
        if self.element == "fire":
            return 300
        if self.element == "ice":
            return 150
        return 0


# don't touch below this line


def main():
    first_dragon = Dragon("fire")
    print(
        f"{first_dragon.element} dragon does {first_dragon.get_breath_damage()} damage"
    )

    second_dragon = Dragon("ice")
    Dragon.element = "fire"
    print(
        f"{second_dragon.element} dragon does {second_dragon.get_breath_damage()} damage"
    )


main()
