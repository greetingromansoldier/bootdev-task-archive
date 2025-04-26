# code before changes:

# def add_prefix(document, documents):
#     prefix = f"{len(documents)}. "
#     new_doc = prefix + document
#     documents.append(new_doc)
#     return documents

# actual code:

def add_prefix(document, documents):
    prefix = f"{len(documents)}. "
    new_doc = prefix + document
    new_elem = (new_doc,)
    documents = documents + new_elem
    return documents
