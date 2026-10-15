# PARENT CLASS
class Library_Materials:
    def __init__(self, title: str, author: str):
        self.__title = title
        self.__author = author

    def set_title(self):
        self.__title = title

    def set_author(self):
        self.__author = author

    def get_title(self):
        return self.__title

    def get_author(self):
        return self.__author

    def display_info(self):
        print(f"Title: {self.__title} \nAuthor: {self.__author}")
        return self.__title, self.__author

# CHILD CLASS 1 - BOOK
class Book(Library_Materials):
    def __init__(self, title: str, author: str, number_of_pages: int):
        super().__init__(title, author)
        self.__number_of_pages = number_of_pages

    def set_number_of_pages(self, number_pages):
        if number_pages >= 0:
            self.__number_of_pages = number_of_pages
        else:
            self.__number_of_pages = self.__number_of_pages
            print("Number of Pages must be Positive")  # Ensures that number_pages wont be set as negative

    def get_number_of_pages(self):
        return self.__number_of_pages

# CHILD CLASS 2 - MAGAZINE
class Magazine(Library_Materials):
    def __init__(self, title: str, author: str, issue_number: int):
        super().__init__(title, author)
        self.__issue_number = issue_number

    def set_issue_number(self, issue_number):
        if issue_number >= 0:
            self.__issue_number = issue_number
        else:
            self.__issue_number = self.__issue_number
            print("Issue number must be positive")  # Ensures that issue_number wont be set as negative
            
    def get_issue_number(self):
        return self.__issue_number

# EXECUTION
def main():
    library_material1 = Library_Materials("Journal of Experimental Psychology", "Ratchiff, R. & Van Dongen, H.")
    book1 = Book("The Hobbit", "J.R.R. Tolkien", 310)
    magazine1 = Magazine("National Geographic", "Various Authors", 202)

    print("Publication Information:")
    library_material1.display_info()

    print("\nBook Information:")
    book1.set_number_of_pages(-310)
    book1.display_info()
    print(book1.get_number_of_pages())

    print("\nMagazine Information:")
    magazine1.display_info()
    print(magazine1.get_issue_number())

main()


