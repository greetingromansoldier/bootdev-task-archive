# code before changes:

# def new_collection(initial_docs):
#    pass

# actual code

def new_collection(initial_docs):
    in_collection = initial_docs.copy()
    def adding_new (document):
        in_collection.append(document)
        return in_collection
    
    return adding_new


