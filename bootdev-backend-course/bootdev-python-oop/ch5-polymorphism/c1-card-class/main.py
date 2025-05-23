# code before changes:

# SUITS = ["Clubs", "Diamonds", "Hearts", "Spades"]

# RANKS = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]


# class Card:
#     def __init__(self, rank, suit):
#         pass

#     def __eq__(self, other):
#         pass

#     def __lt__(self, other):
#         pass

#     def __gt__(self, other):
#         pass

#     # don't touch below this line

#     def __str__(self):
#         return f"{self.rank} of {self.suit}"

# actual code:

SUITS = ["Clubs", "Diamonds", "Hearts", "Spades"]

RANKS = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]


class Card:
    def __init__(self, rank, suit):
        self.__rank = rank
        self.__suit = suit
        self.__rank_index = RANKS.index(self.__rank)
        self.__suit_index = SUITS.index(self.__suit)


    def __eq__(self, other):
        if self.__rank_index == other.__rank_index and self.__suit_index == other.__suit_index:
            return self.__rank == other.__rank and self.__suit == other.__suit
        else:
            return False


    def __lt__(self, other):
        if self.__rank_index < other.__rank_index:
            return True
        elif self.__rank_index == other.__rank_index:
            if self.__suit_index < other.__suit_index:
                return True
            else:
                return False
        else:
            return False

    def __gt__(self, other):
        if self.__rank_index > other.__rank_index:
            return True
        elif self.__rank_index == other.__rank_index:
            if self.__suit_index > other.__suit_index:
                return True
            else:
                return False
        else:
            return False


    # don't touch below this line

    def __str__(self):
        return f"{self.rank} of {self.suit}"
