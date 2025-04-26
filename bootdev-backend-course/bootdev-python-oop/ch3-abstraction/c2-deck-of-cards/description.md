# Deck of Cards

## Assignment

Finish the `DeckOfCards` class. The `SUITS` and `RANKS` of each card have been provided for you as class variables. You won't need to modify them, but you **will** need to use them.

---

### 1. Complete the Constructor
1. Initialize a private empty list called `__cards`.
2. Fill that empty list by calling the `create_deck` method within the constructor.

### 2. Complete the `create_deck(self)` Method
- Create a `(Rank, Suit)` tuple for all 52 cards in the deck.
- Append them to the `__cards` list.
- **Order Matters**:
  - Cards should be ordered by suit in this order: **Hearts**, **Diamonds**, **Clubs**, **Spades**.
  - Within each suit, the ranks should be ordered from **lowest** rank (Ace) to **highest** rank (King).

### 3. Complete the `shuffle_deck(self)` Method
- Use the `random.shuffle()` method (available from the `random` package) to shuffle the cards in the deck.

### 4. Complete the `deal_card(self)` Method
- Use `.pop()` to remove the **first card off the top of the deck** (the **end** of the list).
- Return it.
- If there are **no cards left** in the deck, the method should return `None`.
