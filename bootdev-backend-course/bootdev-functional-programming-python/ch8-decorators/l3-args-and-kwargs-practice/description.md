# Args and Kwargs Practice

Doc2Doc should be extensible to allow for third-party plugins. These plugins will be configurable.

## Assignment

Complete the `configure_plugin_decorator` function. It decorates a `func` that takes keyword arguments `**kwargs`, but the wrapper function it returns takes positional arguments `*args`. The arguments passed to the wrapper will be a series of tuples, each a key/value pair.

1.  Convert the `args` into a dictionary with the `dict` function.
2.  Get the result of passing this dictionary into the `func` as keyword arguments unpacked with the `**` operator.
3.  Return the result.

```python
plugin_config = configure_backups(("path", "~/duplicates"), ("prefix", "duplicate_"), ("extension", ".rtf"))

# plugin_config:
# {
#   "path": "~/duplicates",
#   "prefix": "duplicate_",
#   "extension": ".rtf",
# }

```
