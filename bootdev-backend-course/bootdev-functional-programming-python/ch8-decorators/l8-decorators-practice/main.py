# code before changes:

# def replacer(old, new):
#     pass
#
#
# # ?
# # ?
# # ?
# # ?
# # ?
# def tag_pre(text):
#     return f"<pre>{text}</pre>"

# actual code:

def replacer(old, new):
    def replace (decorated_func):
        def wrapper(text):
            new_text = text.replace(old, new)
            return decorated_func(new_text)
        return wrapper
    return replace


@replacer("&", "&amp;")
@replacer("<", "&lt;")
@replacer(">", "&gt;")
@replacer('"', "&quot;")
@replacer("'", "&#x27;")
def tag_pre(text):
    return f"<pre>{text}</pre>"
