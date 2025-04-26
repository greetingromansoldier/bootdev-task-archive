# code before changes:

# def format_line(line):
#     return f"{line.rstrip().capitalize().replace(',', '')}...."

# actual code:

def format_line(line):
    return f"{line.strip().upper().replace('.', '')}..."
