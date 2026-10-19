class Publication:
    def __init__(self, title, author):
        self.__title = title
        self.__author = author

    def get_title(self):
        return self.__title

    def get_author(self):
        return self.__author

    def set_title(self, title):
        self.__title = title

    def set_author(self, author):
        self.__author = author

    def display_info(self):
        print("Title:", self.__title)
        print("Author:", self.__author)


class Book(Publication):
    def __init__(self, title, author, pages):
        super().__init__(title, author)
        self.__pages = 1
        self.set_pages(pages)

    def get_pages(self):
        return self.__pages

    def set_pages(self, pages):
        if pages > 0:
            self.__pages = pages
        else:
            print("Number of pages must be positive.")

    def display_info(self):
        super().display_info()
        print("Pages:", self.__pages)


class Magazine(Publication):
    def __init__(self, title, author, issue):
        super().__init__(title, author)
        self.__issue = 1
        self.set_issue(issue)

    def get_issue(self):
        return self.__issue

    def set_issue(self, issue):
        if issue > 0:
            self.__issue = issue
        else:
            print("Issue number must be positive.")

    def display_info(self):
        super().display_info()
        print("Issue:", self.__issue)


pub1 = Publication("Science Today", "John Smith")
pub2 = Publication("Technology Weekly", "Jane Doe")

book1 = Book("The Hobbit", "J.R.R. Tolkien", 310)
book2 = Book("Harry Potter", "J.K. Rowling", 350)

mag1 = Magazine("National Geographic", "Various Authors", 202)
mag2 = Magazine("Time Magazine", "Various Authors", 150)

for item in [pub1, pub2, book1, book2, mag1, mag2]:
    item.display_info()
    print()