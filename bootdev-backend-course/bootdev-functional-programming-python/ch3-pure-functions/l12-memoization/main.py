# code before changes:
# def word_count_memo(document, memos):
#     pass


# # Don't edit below this line


# def word_count(document):
#     count = len(document.split())
#     return count

# actual code:

def word_count_memo(document, memos):
    memos_copy = memos.copy()
    if document in memos_copy:
        return memos_copy[document], memos_copy
    else:
        memos_copy[document] = word_count(document)
        return memos_copy[document], memos_copy


# Don't edit below this line


def word_count(document):
    count = len(document.split())
    return count
