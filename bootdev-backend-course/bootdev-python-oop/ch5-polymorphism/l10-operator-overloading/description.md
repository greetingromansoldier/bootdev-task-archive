# Assignment: Sword Crafting with Operator Overloading
#programming #python #oop #operator-overloading #assignment

In Age of Dragons, players can upgrade their weaponry. To make "crafting" simple for other developers, we'll use **operator overloading** on the `Sword` class. Note how the test suite attempts to use the `+` operator to craft the swords. Overload the `+` operator to craft the swords.

## Task

Create an `__add__(self, other)` method on the `Sword` class. It will be used to "craft" two swords together to create a new sword. **Return** a new `Sword` instance.

## Sword Types

`sword_type` is just a string, one of:
- `bronze`
- `iron`
- `steel`

## Crafting Rules

- [ ] 1. If two `"bronze"` swords are crafted together, **return** a new `"iron"` sword.
- [ ] 2. If two `"iron"` swords are crafted together, **return** a new `"steel"` sword.
- [ ] 3. If a player tries to craft anything other than 2 bronze swords or 2 iron swords, just **raise** an `Exception` with the message `"cannot craft"`.
