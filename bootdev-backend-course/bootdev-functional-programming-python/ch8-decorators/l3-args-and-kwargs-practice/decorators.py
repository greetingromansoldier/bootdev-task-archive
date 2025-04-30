# code before changes:

# def configure_plugin_decorator(func):
#     pass

# actual code:

def configure_plugin_decorator(func):

    def wrapper (*args):
        args_dict = dict(args)
        result = func(**args_dict)
        return result

    return wrapper
