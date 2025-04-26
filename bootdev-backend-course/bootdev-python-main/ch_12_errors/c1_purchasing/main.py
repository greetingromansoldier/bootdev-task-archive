# code before changes:

# def purchase_item(price, gold_available):
#     pass

# assignment:

# Complete the purchase_item function. 
# If the character doesn't have enough gold raise an exception with the text not enough gold. 
# Don't handle the exception.

# Otherwise, return the amount of money the customer has leftover after completing the purchase.
# actual code:

def purchase_item(price, gold_available):
    if gold_available < price:
        raise Exception("not enough gold")
    else:
        gold_available -= price
        return gold_available