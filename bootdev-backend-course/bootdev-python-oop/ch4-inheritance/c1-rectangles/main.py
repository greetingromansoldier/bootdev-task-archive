# code before changes:

# class Rectangle:
#     def __init__(self, length, width):
#         pass

#     def get_area(self):
#         pass

#     def get_perimeter(self):
#         pass


# class Square(Rectangle):
#     def __init__(self, length):
#         pass

# actual code:

class Rectangle:
    def __init__(self, length, width):
        self.__length = length
        self.__width = width

    def get_area(self):
        return self.__length * self.__width


    def get_perimeter(self):
        return (self.__length + self.__width) *2


class Square(Rectangle):
    def __init__(self, length):
        super().__init__(length, length)
