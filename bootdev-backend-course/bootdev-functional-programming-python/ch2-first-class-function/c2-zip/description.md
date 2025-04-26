# Assignment

Complete the `pair_document_with_format` function. It takes two lists as input: `doc_names` and `doc_formats`. Each list contains strings. The `doc_names` list contains the names of documents, and the `doc_formats` list contains the file formats of the documents.

First, `zip` up the lists into a single list of tuples with the names as the first index and the formats as the second index in each tuple.

Next, `filter` the list of tuples to only include tuples where the format is one of the given `valid_formats`.

Return the result as a *list*.
