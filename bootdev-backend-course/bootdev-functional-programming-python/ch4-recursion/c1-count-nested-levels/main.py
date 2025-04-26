# code before changes:

# def count_nested_levels(nested_documents, target_document_id, level=1):
#     pass

# actual code:

def count_nested_levels(nested_documents, target_document_id, level=1):
    for document_id in nested_documents:
        if document_id == target_document_id:
            return level
        if document_id != target_document_id:
            func_result = count_nested_levels(nested_documents[document_id], target_document_id, level+1)
            if func_result != -1:
                return func_result
    return -1
