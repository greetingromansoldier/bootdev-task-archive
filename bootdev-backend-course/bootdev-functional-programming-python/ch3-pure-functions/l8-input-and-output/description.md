# Assignment

In Doc2Doc, we frequently need to change the casing of some text. For example:
TitleCase

    Every Day Once A Day Give Yourself A Present

LowerCase

    every day once a day give yourself a present

UpperCase

    EVERY DAY ONCE A DAY GIVE YOURSELF A PRESENT

There is an issue in the convert_case function, our test suite can't test its behavior because it's printing to the console (eww... a side-effect) instead of returning a value. Fix the function so that it returns the correct value instead of printing it.
