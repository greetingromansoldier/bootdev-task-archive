# Sum Types Practice

Doc2Doc should be able to prepare and export a CSV file of whatever data you input. Comma-Separated Values are a ubiquitous text format that allows for information to be structured in a table. There is usually a header row, followed by data rows. Within rows, items are separated by commas.

## Assignment

Complete the `get_csv_status` function. It should use a match case statement to select the correct response depending on the status of the export operation. Create functions to handle each operation as follows:

1.  `PENDING`: return a tuple with the string `"Pending..."` and the data converted from a list of lists of anything, to a list of lists of strings.
    1.  Try to use nested map functions to convert the data items into strings.
    2.  Remember to convert from a map object back into a list.
2.  `PROCESSING`: return a tuple with the string `"Processing..."` and the data converted from a list of lists of strings into one string in CSV format.
    1.  For each list of strings, combine the strings with `join` with commas inbetween to form a row.
    2.  For each row string, combine the strings with `join` with newlines `"\n"` inbetween to form a table.
3.  `SUCCESS`: return a tuple with the string `"Success!"` and simply return the data as is.
4.  `FAILURE`: return a tuple with the string `"Unknown error, retrying..."` and the data after it has been prepared and processed into a CSV string, by combining the steps for `Pending` and `Processing`.
5.  Any Other Status: raise an `Exception` with the string `"unknown export status"`.

## Tip

It's better if you try this challenge without using loops for practice, but you may use loops.
