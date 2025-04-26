# Assignment

Complete the `remove_invalid_lines` function. It accepts a document as input. It should:

1.  Use the built-in `filter` function and a lambda to return a copy of the input document
2.  Remove any lines that start with a `-` character.
3.  Keep all other lines and preserve trailing newlines.

For example, this:

```
* Star Wars episode 1 is underrated
- Star Wars episode 9 is fine
* Star Wars episode 3 is the best
```

Should become:

```
* Star Wars episode 1 is underrated
* Star Wars episode 3 is the best
```

# Tips

The `splitlines` method does not preserve trailing newlines and may cause your output to fail the tests.

The following methods may be useful:

**.join**

```python
"\n".join(["a", "b", "c"])
# a
# b
# c
```

**.startswith**

```python
s = "hello"
s.startswith("h")
# True
s.startswith("o")
# False
```

**.split**

```python
s = """hello
world"""
lines = s.split("\n")
# ['hello', 'world']
```
