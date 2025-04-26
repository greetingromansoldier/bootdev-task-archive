# code before changes:

# def hex_to_rgb(hex_color):
#     # ?
#     r = int(hex_color[:2], 10)
#     g = int(hex_color[2:4], 10)
#     b = int(hex_color[4:], 10)
#     return r, g, b


# actual code:

def hex_to_rgb(hex_color):
    print(f"is_hexadecimal: {is_hexadecimal(hex_color)}")
    if is_hexadecimal(hex_color) == False or len(hex_color) != 6:
        raise Exception ("not a hex color string")

    r = int(hex_color[:2], 16)
    g = int(hex_color[2:4], 16)
    b = int(hex_color[4:], 16)
    return r, g, b


# Don't edit below this line


def is_hexadecimal(hex_string):
    try:
        int(hex_string, 16)
        return True
    except Exception:
        return False
