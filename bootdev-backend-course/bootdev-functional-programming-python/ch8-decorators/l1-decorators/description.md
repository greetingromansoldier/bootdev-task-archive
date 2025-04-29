## Assignment

The provided `file_type_aggregator` function is intended to decorate other functions. It assumes that the function it decorates has exactly 2 positional arguments.

**Create a `process_doc` function** that's decorated by `file_type_aggregator`. It should return the following string:

```python
f"Processing doc: '{doc}'. File Type: {file_type}"
```

Where `doc` and `file_type` are its positional arguments. (See line 11 for where it's being called)
