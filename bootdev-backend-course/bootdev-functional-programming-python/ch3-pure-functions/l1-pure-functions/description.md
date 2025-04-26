# Assignment

There's a bug in the convert_file_format function! Right now, it relies on data outside its own scope. These global values can be changed by other parts of the code, so they are not guaranteed to be the same every time convert_file_format is called.

Fix the bug by making convert_file_format a pure function. It should only depend on data that is scoped inside of the function.
