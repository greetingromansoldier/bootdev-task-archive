## Assignment

Whenever a document is parsed by Doc2Doc, it can either succeed or fail. In functional programming, we often represent errors as data (e.g. the `ParseError` class) rather than by `raise`ing exceptions, because exceptions are side effects. *(This isn't standard Python practice, but it's useful to understand from an FP perspective)*

**Complete the `Parsed` and `ParseError` subclasses.**

*   `Parsed` represents success. It should accept a `doc_name` string and a `text` string and save them as properties of the same name.
*   `ParseError` represents failure. It should accept a `doc_name` string and an `err` string and save them as properties of the same name.

The test suite uses the `isinstance` function to see if an error occurred based on the class type.
