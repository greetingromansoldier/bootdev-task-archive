# YES LOGGER IS THE NAME PROVIDED TO THIS FILE IN ORIGINAL COURSE BY AUTHORS
# code before changes:

# def args_logger(*args, **kwargs):
#     # ?

# actual code

def args_logger(*args, **kwargs):
    sorted(args, key=str)
    for i in range(0, len(args)):
        print(f"{i+1}. {str(args[i])}")
    kwargs = sorted(kwargs.items())
    for kwarg in kwargs:
        print(f"* {kwarg[0]}: {kwarg[1]}")
