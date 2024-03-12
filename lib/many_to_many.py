import ipdb

class Author:

    def __init__(self,name):
        self.name = name

class Book:
    def __init__(self,title):
        self.title = title


class Contract:
    def __init__(self,author,book,date,royalties):
        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties





jk_rowling = Author('jk rowling')


print(jk_rowling.name)