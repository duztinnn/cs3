class Publication:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def set_author(self, author):
        self.author = author

    def get_author(self):
        return self.author

    def set_title(self, title):
        self.title = title

    def get_title(self):
        return self.title

    def display_info(self):
        print("Title: ", self.title)
        print("Author: ", self.author)


class Book(Publication):
    def __init__(self, title, author, number_pages):
        self.number_pages = number_pages
        self.title = title
        self.author = author

    def set_number_of_pages(self, number_pages):
        if number_pages > 0:
            self.number_pages = number_pages
        elif number_pages < 0:
            print("The number of pages must be positive")

    def get_number_of_pages(self):
        return self.number_pages

    def display_info(self):
        print("Book Information:")
        print("Title: ", self.title)
        print("Author: ", self.author)
        #print("Number of pages: ", self.number_pages)
       

    
class Magazine(Publication):
    def __init__(self, title, author, issue_number):
        self.issue_number = issue_number
        self.title = title
        self.author = author

    def set_issue_number(self, issue_number):
        if issue_number > 0:
            self.issue_number = issue_number
        elif issue_number < 0:
            print("The issue number must be positive")

    def get_issue_number(self):
        return self.issue_number

    def display_info(self):
        print("Magazine Information:")
        print("Title: ", self.title)
        print("Author: ", self.author)
        #print("Number of pages: ", self.issue_number)
        


pub1 = Publication("Journal of Experimental Psychology", "Ratchiff, R. & Van Dongen, H.")
book1 = Book("The Hobbit", "J.R.R Tolkien", 310)
mag1 = Magazine("National Geographic", "Various Authors", 202)

print("Publication Information:")
pub1.display_info()

print("")
book1.set_number_of_pages(310)
book1.display_info()
print("Number of pages: ", book1.get_number_of_pages())

print("")
mag1.set_issue_number(202)
mag1.display_info()
print("Issue number: ", mag1.get_issue_number())
