# code before changes:

# def main():
#     # ?

# assignment:

# Take a look at the Brawler class and the fight function provided.

# In the main function:

#     Create 4 new brawlers with the following stats:
#         Name: Aragorn. Speed: 4. Strength: 4.
#         Name: Gimli. Speed: 2. Strength: 7.
#         Name: Legolas. Speed: 7. Strength: 7.
#         Name: Frodo. Speed: 3. Strength: 2.
#     Call fight twice.
#         The first fight should be Aragorn vs Gimli.
#         The second will be Legolas vs Frodo.

# actual code:

def main():
    aragorn = Brawler("Aragorn", 4, 4)
    gimli = Brawler("Gimli", 2, 7)
    legolas = Brawler("Legolas", 7, 7)
    frodo = Brawler("Frodo", 3, 2)

    fight(aragorn, gimli)
    fight(legolas, frodo)


# don't touch below this line


class Brawler:
    def __init__(self, name, speed, strength):
        self.name = name
        self.speed = speed
        self.strength = strength
        self.power = speed * strength


def fight(f1, f2):
    if f1.power > f2.power:
        print(f"{f1.name} wins with {f1.power} power over {f2.name}'s {f2.power}")
    elif f1.power < f2.power:
        print(f"{f2.name} wins with {f2.power} power over {f1.name}'s {f1.power}")
    else:
        print(f"It's a tie with both contestants at {f1.power} power")


main()
