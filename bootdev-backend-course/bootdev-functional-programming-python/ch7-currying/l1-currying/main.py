# code before changes:

# def converted_font_size(font_size, doc_type):
#     if doc_type == "txt":
#         return font_size
#     if doc_type == "md":
#         return font_size * 2
#     if doc_type == "docx":
#         return font_size * 3
#     raise ValueError("invalid doc type")
#

# actual code

def converted_font_size(font_size):
    
    def doc_choosing (doc_type):
        if doc_type == "txt":
            return font_size
        if doc_type == "md":
            return font_size * 2
        if doc_type == "docx":
            return font_size * 3
        raise ValueError("invalid doc type")

    return doc_choosing




