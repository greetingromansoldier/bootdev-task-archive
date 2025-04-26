# code before changes:

# def print_numbers():
#     for :
#         print(i)

# assignment:

# Complete the missing sections of the for-loop in the print_numbers function 
# so that it prints the numbers 0-99 to the console.

# actual code: 

def print_numbers():
    for i in range (0, 100):
        print(i)


# Don't edit below this line


def test():
    print("Printing numbers from 0 to 99:")
    print_numbers()
    print("=====================================")


def main():
    test()


main()