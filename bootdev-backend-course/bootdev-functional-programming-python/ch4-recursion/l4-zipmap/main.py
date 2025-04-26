# code before changes:

# def zipmap(keys, values):
#     pass

# actual code:
def zipmap(keys, values):
    dictionary = {}
    if len(keys) == 0 or len(values) == 0:
        return dictionary

    result = zipmap(keys[1:], values[1:])
    print(result)
    result[keys[0]] = values[0]
    return result
