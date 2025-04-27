# code before changes:

# def get_filter_cmd(filter_one, filter_two):
#     def filter_cmd(content, option):
#         pass

#     return filter_cmd

# actual code:

def get_filter_cmd(filter_one, filter_two):
    def filter_cmd(content, option="--one"):
        if option in {"--one"}:
            return filter_one(content)
        elif option in {"--two"}:
            return filter_two(content)
        elif option in {"--three"}:
            return filter_two(filter_one(content))
        raise Exception("invalid option")



    return filter_cmd

# don't touch below this line


def replace_bad(text):
    return text.replace("bad", "good")


def replace_ellipsis(text):
    return text.replace("..", "...")


def fix_ellipsis(text):
    return text.replace("....", "...")
