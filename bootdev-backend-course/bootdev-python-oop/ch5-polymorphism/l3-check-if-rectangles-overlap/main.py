# code before changes:

# class Rectangle:
#     def overlaps(self, rect):
#         pass

# actual code:

class Rectangle:
    def overlaps(self, rect):
        check_x = False
        check_y = False

        for i in range(self.get_left_x(), self.get_right_x()+1):
            if i in range(rect.get_left_x(), rect.get_right_x()+1):
                check_x = True
        for i in range(self.get_bottom_y(), self.get_top_y()+1):
            if i in range(rect.get_bottom_y(), rect.get_top_y()+1):
                check_y = True

        if check_x == True and check_y == True:
            return True
        else:
            return False


    # don't touch below this line

    def __init__(self, x1, y1, x2, y2):
        self.__x1 = x1
        self.__y1 = y1
        self.__x2 = x2
        self.__y2 = y2

    def get_left_x(self):
        if self.__x1 < self.__x2:
            return self.__x1
        return self.__x2

    def get_right_x(self):
        if self.__x1 > self.__x2:
            return self.__x1
        return self.__x2

    def get_top_y(self):
        if self.__y1 > self.__y2:
            return self.__y1
        return self.__y2

    def get_bottom_y(self):
        if self.__y1 < self.__y2:
            return self.__y1
        return self.__y2

    def __repr__(self):
        return f"Rectangle({self.__x1}, {self.__y1}, {self.__x2}, {self.__y2})"
