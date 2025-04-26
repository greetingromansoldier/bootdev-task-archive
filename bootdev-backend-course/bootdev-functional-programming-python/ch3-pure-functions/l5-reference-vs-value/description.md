# Assignment

We have a way for Doc2Doc users to set their supported formats in their settings. In memory, we store those settings as a simple dictionary:

```python
settings = {
    "docx": True,
    "pdf": True,
    "txt": False
}
```

Unfortunately, there is a bug in our code! When a new format is added or removed, it not only updates the new dictionary, but it changes the defaults themselves! That's not good. We want to create a *new* dictionary with the updates, not change the original.

Fix the bug by making `add_format` and `remove_format` pure functions that don't mutate their inputs.

# Tip

Simply assigning a new variable to an existing dictionary doesn't copy that dictionary, it points to the same dictionary. Instead use the `.copy()` method to create a new copy of a dictionary.
