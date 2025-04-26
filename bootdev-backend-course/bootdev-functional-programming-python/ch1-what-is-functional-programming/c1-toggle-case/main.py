# code before changes:

# def toggle_case(line):
#     if line.istitle():
#         pass
#     if line.isupper():
#         pass
#     if len(line) > 0 and line[1:].islower():
#         pass

# actual code:

def toggle_case(line):
    if line.istitle():
        return f"{line.upper()}" + "!!!"
    elif line.isupper():
        return f'{line.lower().replace("!","").capitalize()}'
    elif len(line) > 0 and line[1:].islower():
        return line.title()
    else:
        return line
