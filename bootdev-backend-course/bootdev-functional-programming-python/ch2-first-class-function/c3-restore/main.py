# code before changes:

# def restore_documents(originals, backups):
#     pass

# actual code:

def restore_documents(originals, backups):
    return set(filter(lambda x: not x.isdigit(), map(lambda x: x.upper(), originals + backups)))
