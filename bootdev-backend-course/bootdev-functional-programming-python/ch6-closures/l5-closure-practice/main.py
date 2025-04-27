# code before changes:

# def css_styles(initial_styles):
#     pass

# actual code


def css_styles(initial_styles):
    initial_styles_cp = initial_styles.copy()
    def add_style(selector, property, value):
        if selector not in initial_styles_cp:
            initial_styles_cp[selector] = {}
        initial_styles_cp[selector][property] = value
        return initial_styles_cp
    
    return add_style


