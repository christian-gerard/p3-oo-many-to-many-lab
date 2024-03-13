import ipdb

class Author:
    all = []

    def __init__(self,name):
        self.name = name
        self.all.append(self)


    def contracts(self):
        return [contract for contract in Contract.all if contract.author.name == self.name ]

    def books(self):
        return [ contract.book for contract in Contract.all if contract.author.name == self.name ]
    
    def sign_contract(self,book,date,royalties):
        return Contract(self,book,date,royalties)

    def total_royalties(self):
        royalties = [contract.royalties for contract in Contract.all if contract.author.name == self.name]
        sum = 0
        for money in royalties:
            sum += money
        return sum

class Book:
    all = []

    def __init__(self,title):
        self.title = title
        self.all.append(self)

    def contracts(self):
        return [ contract for contract in Contract.all if contract.book.title == self.title ]

    def authors(self):
        return [ contract.author for contract in Contract.all if contract.book.title == self.title]

class Contract:
    all = []

# Switch to properties
    def __init__(self,author,book,date,royalties):
        if not isinstance(author, Author):
            raise Exception
        else:
            self.author = author 
        if not isinstance(book,Book):
            raise Exception
        else:
            self.book = book
        if not isinstance(date, str):
            raise Exception
        else:
            self.date = date
        if not isinstance(royalties, int):
            raise Exception
        else:
            self.royalties = royalties
        self.all.append(self)

    def contracts_by_date(date):
        return [ contract for contract in Contract.all if contract.date == date]










rowling = Author('JK Rowling')
king = Author('Stepehen King')
harry_potter = Book('Harry Potter')
chamber_of_secrets = Book('Chamber of Secrets')

scholastic = Contract(rowling,harry_potter,'01-03-1997',25)
penguin = Contract(rowling,chamber_of_secrets,'01-03-1997',25)

print(rowling.total_royalties())