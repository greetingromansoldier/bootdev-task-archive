class Wizard:
    def __init__(self, name, stamina, intelligence):
        self.__stamina__ = stamina
        self.__intelligence__ = intelligence
        self.name = name
        self.health = stamina * 100
        self.mana = intelligence * 10
