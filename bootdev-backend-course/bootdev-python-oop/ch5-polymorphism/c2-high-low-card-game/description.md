# High-Low Card Game

Let's extend the `Card` logic we built to make a simple high-card low-card game.

## Assignment

We will be building a simple game where we compare two cards and depending on the round (high or low) determine the winner.

1.  `HighCardRound`: The highest card wins
2.  `LowCardRound`: The lowest card wins
3.  [ ] Complete the `HighCardRound` class that inherits from `Round`:
    *   [ ] Create a constructor that takes two cards (`card1` and `card2`) and stores them as instance variables.
    *   [ ] Implement the `resolve_round()` method that returns:
        *   `1` if `card1` is higher than `card2`
        *   `2` if `card2` is higher than `card1`
        *   `0` if the cards are equal
4.  [ ] Complete the `LowCardRound` class that inherits from `Round`:
    *   [ ] Create a constructor that takes two cards (`card1` and `card2`) and stores them as instance variables.
    *   [ ] Implement the `resolve_round()` method that returns:
        *   `1` if `card1` is lower than `card2`
        *   `2` if `card2` is lower than `card1`
        *   `0` if the cards are equal
