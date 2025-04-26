
Assignment

In the world of document conversion, we sometimes need to handle fonts and font sizes.

Complete the get_median_font_size function. Given a list of numbers representing font sizes, return the median of the list.

For example:

```
[1, 2, 3] => 2
[10, 8, 7, 5] => 7
```

Notice the second list is out of order. Order the list, then find the middle index, and return the middle number. If there is an even amount of numbers, return the smaller of the two middle numbers (I know it's not a true median, but good for our purposes). If the list is empty, just return None.

Here are some helpful docs:

- sorted
- len
- // (floor division)

To be a good little functional programmer, your code for this lesson should not:

- Use loops
- Mutate any variables (it's okay to create new ones)
