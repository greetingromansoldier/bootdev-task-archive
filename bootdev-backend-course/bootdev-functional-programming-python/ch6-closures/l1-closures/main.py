# code before changes:

# def word_count_aggregator():
#     pass

# actual code:

def word_count_aggregator():
    count = 0
    def calculate(doc):
        words_count = len(doc.split())
        nonlocal count
        count += words_count
        return count

    return calculate
