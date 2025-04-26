# code before changes:

# class Calculator:
#     def __init__(self):
#         pass

#     def add(self, a):
#         pass

#     def subtract(self, a):
#         pass

#     def multiply(self, a):
#         pass

#     def divide(self, a):
#         pass

#     def modulo(self, a):
#         pass

#     def power(self, a):
#         pass

#     def square_root(self):
#         pass

#     def clear(self):
#         pass

#     def get_result(self):
#         pass

# actual code:

class Calculator:
    def __init__(self):
        self.__result = 0

    def add(self, a):
        self.__result += a

    def subtract(self, a):
        self.__result -= a

    def multiply(self, a):
        self.__result *= a

    def divide(self, a):
        if a == 0:
            raise ValueError ("cannot divide by zero")

        self.__result /= a

    def modulo(self, a):
        if a == 0:
            raise ValueError ("cannot divide by zero")

        self.__result %= a

    def power(self, a):
        self.__result **= a

    def square_root(self):
        self.__result **= 0.5

    def clear(self):
        self.__result = 0

    def get_result(self):
        return self.__result
