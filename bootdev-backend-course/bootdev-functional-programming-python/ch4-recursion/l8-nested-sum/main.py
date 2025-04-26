# code before changes:

# def sum_nested_list(lst):
#     pass

# actual code:

def sum_nested_list(lst):
    sum = 0
    for item in lst:
        if isinstance(item, list) == False:
            sum += item
        else:
            lst_sum = sum_nested_list(item)
            sum += lst_sum

    return sum
