# code before changes:

# def countdown_to_start():
#     # ?

# assignment:

# In the countdown_to_start function, write a loop that counts down from 10 to 1. 
# At each iteration, print the number with an ellipsis:

# i...

# However, when i is 1, it should print 1...Fight! instead.

# Do not use the ellipsis (…) character. Use three periods (...) instead.

# actual code:

def countdown_to_start():
    for i in range (10, 0, -1):
        if i == 1:
            return (print(f"{i}...Fight!"))
        else:
            print(f"{i}...")
    
        


# Don't edit below this line


def test():
    print("Counting down to match start:")
    countdown_to_start()
    print("=====================================")


def main():
    test()


main()