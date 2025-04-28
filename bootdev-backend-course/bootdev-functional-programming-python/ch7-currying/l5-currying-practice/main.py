# code before changes:
#
# def create_markdown_image(alt_text):
#     pass
#
# actual code:

def create_markdown_image(alt_text):
    new_alt_text = "!" + "[" + alt_text + "]"

    def inner_url(url):
        # there is no need for nonlocal if you create new variable in inner f-ns, it rather my mistake
        nonlocal new_alt_text 

        url = "(" + url.replace("(", "%28").replace(")", "%29") + ")"
        new_alt_text = new_alt_text + url

        def innermost_title(title=""):
            nonlocal new_alt_text

            if title != "":
                title = '"' + title + '"'
                new_alt_text = new_alt_text.rstrip(")") + " " + title + ")"

            return new_alt_text

        return innermost_title

    return inner_url

