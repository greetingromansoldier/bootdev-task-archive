# code before changes:

# class Archer:
#     def __init__(self, name, health, num_arrows):
#         pass

#     def get_shot(self):
#         pass

#     def shoot(self, target):
#         pass

#     # don't touch below this line

#     def get_status(self):
#         return self.name, self.health, self.num_arrows

#     def print_status(self):
#         print(f"{self.name} has {self.health} health and {self.num_arrows} arrows")


# assignment:

# Complete the Archer class.

#     1) Create the constructor, which should take the following parameters in order and set them as properties:
#         1.1)  name
#         1.2)  health
#         1.3)  num_arrows

#     2) Complete the get_shot method. It operates on the current archer instance.
#         2.1) If the current archer has health left, remove one health from the current archer.
#         2.2) After the above check, if the archer's health is 0, raise the exception: {} is dead where {} is the archer's name.

#     3) Finish the shoot method. It takes an Archer instance as the target input.
#         3.1) If the shooter has no arrows left, raise the exception {} can't shoot where {} is the shooter's name.
#         3.2) Otherwise, remove an arrow from the shooter.
#         3.3) Print {1} shoots {2} where {1} is the shooter's name and {2} is the name of the targeted archer.
#         3.4) Call the target's get_shot() method.


# actual code:


class Archer:
    def __init__(self, name, health, num_arrows):
        self.name = name
        self.health = health
        self.num_arrows = num_arrows

    def get_shot(self):
        if self.health > 0:
            self.health -= 1

        if self.health == 0:
            raise Exception(f"{self.name} is dead")

    def shoot(self, target):
        if self.num_arrows == 0:
            raise Exception(f"{self.name} can't shoot")

        self.num_arrows -= 1

        print(f"{self.name} shoots {target.name}")
        target.get_shot()


    # don't touch below this line

    def get_status(self):
        return self.name, self.health, self.num_arrows

    def print_status(self):
        print(f"{self.name} has {self.health} health and {self.num_arrows} arrows")
