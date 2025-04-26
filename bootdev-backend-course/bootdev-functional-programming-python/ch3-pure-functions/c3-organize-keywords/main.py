# code before changes:

# keywords = [
#     "functional",
#     "immutable",
#     "declarative",
#     "higher-order",
#     "lambda",
#     "deterministic",
#     "side-effects",
#     "memoization",
#     "referential transparency",
# ]


# def map_keywords(document, document_map):
#     if document in document_map:
#         return document_map[document], document_map
#     found_keywords = find_keywords(document)
#     document_map[document] = found_keywords
#     return found_keywords, document_map


# def find_keywords(document):
#     pass

# actual code:



def map_keywords(document, document_map):
    document_map = document_map.copy()
    if document in document_map:
        return document_map[document], document_map
    found_keywords = find_keywords(document)
    document_map[document] = found_keywords
    return found_keywords, document_map


def find_keywords(document):
    keywords = [
        "functional",
        "immutable",
        "declarative",
        "higher-order",
        "lambda",
        "deterministic",
        "side-effects",
        "memoization",
        "referential transparency",
    ]

    return list(filter(lambda keyword: keyword in document.lower(), keywords))
