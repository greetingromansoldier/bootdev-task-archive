# code before changes:
#
# def lines_with_sequence(char):
#     def with_char(length):
#         sequence = char * length
#
#         # ?
#
#     return with_char
#
# actual code:

def lines_with_sequence(char):
    def with_char(length):
        sequence = char * length
        def with_length (doc):
            doc = doc.split("\n")
            n_lines = 0
            for n in doc:
                if sequence in n:
                    n_lines += 1
            return n_lines
        return with_length
    return with_char

