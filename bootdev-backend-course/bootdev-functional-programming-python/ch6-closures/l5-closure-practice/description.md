# Closure Practice

Doc2Doc should be able to add css styling to an html file. CSS uses selectors to identify the html element to add the style property. Essentially, styles are a chain of keys and values.

Complete the `css_styles` function. It accepts a nested dictionary as input, `initial_styles`, and returns a function, `add_style`.

1.  [ ] Copies `initial_styles` to avoid modifying the original dictionary.
2.  [ ] Returns an `add_style` function that:
    1.  [ ] Takes three string arguments: `selector`, `property`, and `value`. `selector` is a key in the `initial_styles` dictionary and its value should be a dictionary.
    2.  [ ] Checks if the `selector` exists in the dictionary. If not, creates a new dictionary for the `selector` value.
    3.  [ ] Then adds or updates the `property` with the given `value` for the selector.
    4.  [ ] Returns the updated dictionary.

For example:

```python
initial_styles = {
    "body": {
        "background-color": "white",
        "color": "black"
    },
    "h1": {
        "font-size": "16px",
        "padding": "10px"
    }
}

add_style = css_styles(initial_styles)

new_styles = add_style("p", "color", "grey")
# {
#     "body": {
#         "background-color": "white",
#         "color": "black"
#     },
#     "h1": {
#         "font-size": "16px",
#         "padding": "10px"
#     },
#     "p": {
#         "color": "grey",
#     }
# }
```
