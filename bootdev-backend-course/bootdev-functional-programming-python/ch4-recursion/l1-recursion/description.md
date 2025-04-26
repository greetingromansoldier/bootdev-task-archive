# Assignment

Doc2Doc can automatically generate various layouts for a page. There are a *lot* of possible layouts, so we need a [factorial](https://en.wikipedia.org/wiki/Factorial) function to calculate the total number of possible layouts.

> A factorial is the product of all positive integers less than or equal to a number. For example, `5!` (read: "five factorial") is `5 * 4 * 3 * 2 * 1`, which is `120`.

Complete the `factorial_r` function. It should recursively calculate the factorial of a number.

# Tips

1.  What's a small problem you can solve first?
2.  How can you go from the "first" value of `x` to the "next" value of `x`, all the way down to the "last" value of `x`?
3.  What's the base case that should stop the recursion?
4.  Since `0!` is an [empty product](https://en.wikipedia.org/wiki/Empty_product), what should an input of `0` return?
