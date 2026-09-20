#!/usr/bin/env python3

class Author:
    all = []

    def __init__(self, name):
        self.name = name
        Author.all.append(self)

    def contracts(self):
        # All Contract objects where this author is the author.
        return [contract for contract in Contract.all if contract.author == self]

    def books(self):
        # All Book objects tied to this author, found through Contract
        # acting as the intermediary between Author and Book.
        return [contract.book for contract in Contract.all if contract.author == self]

    def sign_contract(self, book, date, royalties):
        # Creates (and returns) a new Contract linking this author to a book.
        return Contract(self, book, date, royalties)

    def total_royalties(self):
        # Sums royalties across every contract this author has signed.
        return sum(contract.royalties for contract in self.contracts())


class Book:
    all = []

    def __init__(self, title):
        self.title = title
        Book.all.append(self)

    def contracts(self):
        # All Contract objects where this book is the book.
        return [contract for contract in Contract.all if contract.book == self]

    def authors(self):
        # All Author objects tied to this book, through Contract.
        return [contract.author for contract in Contract.all if contract.book == self]


class Contract:
    all = []

    def __init__(self, author, book, date, royalties):
        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        # Only reached if none of the property setters above raised —
        # so an invalid Contract never gets added to Contract.all.
        Contract.all.append(self)

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, author):
        if not isinstance(author, Author):
            raise Exception("author must be an instance of Author")
        self._author = author

    @property
    def book(self):
        return self._book

    @book.setter
    def book(self, book):
        if not isinstance(book, Book):
            raise Exception("book must be an instance of Book")
        self._book = book

    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, date):
        if not isinstance(date, str):
            raise Exception("date must be a string")
        self._date = date

    @property
    def royalties(self):
        return self._royalties

    @royalties.setter
    def royalties(self, royalties):
        if not isinstance(royalties, int):
            raise Exception("royalties must be an integer")
        self._royalties = royalties

    @classmethod
    def contracts_by_date(cls, date):
        # Returns every contract matching the given date, in the order
        # they were originally created.
        return [contract for contract in cls.all if contract.date == date]