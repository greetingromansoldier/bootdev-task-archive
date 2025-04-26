# code before changes:

# def calculate_total(items_purchased, pinned_list):
#     item_prices = {
#         "health_potion": 10.00,
#         "mana_potion": 12.00,
#         "gold_dust": 5.00,
#         "dwarven_ale": 8.00,
#         "enchanted_scroll": 25.00,
#         "ice_cold_milk": 50.00,
#         "herbs": 7.00,
#         "crystal_shard": 20.00,
#         "magic_ring": 100.00,
#         "mystic_amulet": 150.00,
#     }

#     # Don't touch above this line

#     pass

# assignment:

# Complete the calculate_total function.

# Inputs:
#    1)  items_purchased: A list of the names of items purchased. This is a list of strings.
#    2)  pinned_list: A list of the names of items the player has 'pinned' and wanted to purchase. This is also a list of strings.

# Outputs:

# The function should return 3 values in this order:

#    1)  unpurchased_items: A list of all the item names in pinned_list that weren't found in items_purchased, 
#     in the same order that they originally appeared in the pinned_list.
  
#    2)  receipt: A dictionary containing all the items the player purchased, even stuff not on their pinned_list. 
#     The keys are the item names and the values are their respective prices from the item_prices dictionary.
  
#    3)  total: The total cost of all the items that were purchased.

# Return each value separately, not in a singular list. For example:

# return value1, value2, value3
 

# actual code:

def calculate_total(items_purchased, pinned_list):
    item_prices = {
        "health_potion": 10.00,
        "mana_potion": 12.00,
        "gold_dust": 5.00,
        "dwarven_ale": 8.00,
        "enchanted_scroll": 25.00,
        "ice_cold_milk": 50.00,
        "herbs": 7.00,
        "crystal_shard": 20.00,
        "magic_ring": 100.00,
        "mystic_amulet": 150.00,
    }

    # Don't touch above this line

    unpurchased_items = []
    receipt = {}
    total_sum = 0
    for item in pinned_list:
        if item not in items_purchased:
            unpurchased_items.append(item)

    for item in items_purchased:
        receipt[item] = item_prices[item]

    for item in receipt:
        total_sum += item_prices[item]
    
    return unpurchased_items, receipt, total_sum