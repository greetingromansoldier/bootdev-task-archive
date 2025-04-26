# code before changes:

# def convert_case(text, target_format):
#     if not text or not target_format:
#         raise ValueError(f"no text or target format provided")

#     if target_format == "uppercase":
#         print(text.upper())
#         return
#     if target_format == "lowercase":
#         print(text.lower())
#         return
#     if target_format == "titlecase":
#         print(text.title())
#         return
#     raise ValueError(f"unsupported format: {target_format}")

# actual code:

def convert_case(text, target_format):
    if not text or not target_format:
        raise ValueError(f"no text or target format provided")

    if target_format == "uppercase":
        return text.upper()
    if target_format == "lowercase":
        return text.lower()
    if target_format == "titlecase":
        return text.title()
    raise ValueError(f"unsupported format: {target_format}")
