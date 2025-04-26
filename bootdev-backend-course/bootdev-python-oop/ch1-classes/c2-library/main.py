# code before changes:

# class Book:
#     def __init__(self, title, author):
#         pass


# class Library:
#     def __init__(self, name):
#         pass

#     def add_book(self, book):
#         pass

#     def remove_book(self, book):
#         pass

#     def search_books(self, search_string):
#         pass

# actual code:

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author


class Library:
    def __init__(self, name):
        self.name = name
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    # here my error was in lack of understanding objects nature and I tried to delete self.book or sth
    # however, I only needed to delete input (book), which already was kind of object to consider
    def remove_book(self, book):
        for book in self.books:
            if book in self.books and book in self.books:
                self.books.remove(book)





    def search_books(self, search_string):

        def get_keywords (book_object):
            # at first I for some reason parsed all the books into one list which contained all the search words for all books
            # this was really the main problem
            keywords = []

            book_title_split = book.title.split()
            for word in book_title_split:
                keywords.append(word)

            book_author_split = book.author.split()
            for word in book_author_split:
                keywords.append(word)

            return keywords

        # here at first I've initialized list in for loop and it caused error because it was referenced before assignment
        search_results = []
        for book in self.books:
            for word in get_keywords(self.books):
                    if search_string.lower() == word.lower():
                        search_results.append(book)



        return search_results

# here solution from authors of the course (I added only what is different from mine)

    # def remove_book(self, book):
    #     for lib_book in self.books:
    #         if book.title == lib_book.title and book.author == lib_book.author:
    #             self.books.remove(lib_book)

    # def search_books(self, search_string):
    #     results = []
    #     for book in self.books:
    #         if (
    #             search_string.lower() in book.title.lower()
    #             or search_string.lower() in book.author.lower()
    #         ):
    #             results.append(book)
    #     return results
