# Assignment

Complete the new_collection function. It accepts a list of strings, `initial_docs`.

It should return a function that *closes over* a *copy* of `initial_docs`. This function should accept a string, append that string to the closed-over list, and return the new list.

Do *not* modify the original `initial_docs` list!

# Example Usage

```python
new_collection = new_collection(["doc1", "doc2", "doc3"])
print(new_collection("doc4"))
# ['doc1', 'doc2', 'doc3', 'doc4']
print(new_collection("doc5"))
# ['doc1', 'doc2', 'doc3', 'doc4', 'doc5']
```
