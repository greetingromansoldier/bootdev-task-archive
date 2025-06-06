# Count Nested Levels

In Doc2Doc, we might have documents nested inside other documents, forming a kind of tree. You know how crazy `.docx` files can get...

Anyways, we want to find out how deeply nested a given document is.

# Assignment

Complete the `count_nested_levels` function.

1.  [ ] Loop over `document_id`s in the `nested_documents` dictionary
2.  [ ] If the current `document_id` matches the `target_document_id`, return its `level` of nesting
3.  [ ] If the `target_document_id` is not found, recursively call `count_nested_levels` on the current `document_id` and increment the `level`
    *   [ ] If it found the `target_document_id`'s level, return it
4.  [ ] If the `target_document_id` doesn't exist, the function should return `-1`

# Example

In this dictionary, the document with id `3` is nested 2 levels deep. Document `2` is nested 1 level deep.

```python
{
    1: {
        3: {}
    },
    2: {}
}
```
