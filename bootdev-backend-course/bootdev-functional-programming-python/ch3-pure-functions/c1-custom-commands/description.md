# Custom Commands

Doc2Doc is customizable. New commands can be configured to use whichever function suits the user. However, the new commands are causing bugs in other parts of the application by mutating global values and other unintended side effects.

# Assignment

Fix the functions `add_custom_command`, `add_format`, `save_document` and `add_line_break` to make them pure functions without side effects. Here are the reported issues:

*   `add_custom_command`: is an impure function that is mutating an input
*   `add_format`: is an impure function that is mutating an input
*   `save_document`: is an impure function that is mutating an input
*   `add_line_break`: is a no-op function with a side-effect
