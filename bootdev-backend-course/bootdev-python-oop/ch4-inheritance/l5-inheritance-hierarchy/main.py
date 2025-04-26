# code before changes:

# class Archer(Human):
#     def __init__(self, name, num_arrows):
#         super().__init__(name)
#         self.__num_arrows = num_arrows

#     def get_num_arrows(self):
#         return self.__num_arrows

#     def use_arrows(self, num):
#         pass


# class Crossbowman(Archer):
#     def __init__(self, name, num_arrows):
#         pass

#     def triple_shot(self, target):
#         pass

# actual code:

class Human:
    def __init__(self, name):
        self.__name = name

    def get_name(self):
        return self.__name


## don't touch above this line


class Archer(Human):
    def __init__(self, name, num_arrows):
        super().__init__(name)
        self.__num_arrows = num_arrows

    def get_num_arrows(self):
        return self.__num_arrows

    def use_arrows(self, num):
        if num > self.__num_arrows:
            raise Exception ("not enough arrows")

        self.__num_arrows -= num


class Crossbowman(Archer):
    def __init__(self, name, num_arrows):
        super().__init__(name, num_arrows)

    def triple_shot(self, target):
        self.use_arrows(3)
        target_name = target.get_name()
        return f"{target_name} was shot by 3 crossbow bolts"
