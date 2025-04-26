# code before changes:

# def file_to_prompt(file, to_string):
#     # ?

# actual code:

def file_to_prompt(file, to_string):
    return f"```\n{to_string(file)}\n```"
