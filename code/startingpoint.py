#!/usr/local/bin/python3.2
"""
This is a starting point for our library management system
"""
import pickle
import os.path
import time

class Book:
    def __init__(self):
        self.title = ''
        self.author = ''
        self.isbn = ''


class Library:
    """
    represents a collection of books/things
    """
    def __init__(self, filename):
        self.books = {}
        self.filename = filename

    def Keys(self, Keys):
        Keys = ['title','author','isbn']

    def add_book(self, book):
        """
        add a book to the library
        """
        self.books[time.time()] = book
        
    def remove_book(self, book):
        """
        remove a book from the library
        """
        pass
    
    def find_book(self, title):
        """
        return the book with the given title
        """
        pass
    
    def get_all_books(self):
        """
        return a list of all the books
        """
        for book in self.books:
            print(self.book)
    
    def save(self):
        """
        saves the library
        """
        with open(self.filename, 'wb') as fp:
            pickle.dump(self, fp)
        
    def load(filename):
        if os.path.exists(filename):
            with open(filename, 'rb') as fp:
                return pickle.load(fp)
        else:
            # if it doesn't exist, create a new instance of the library
            return Library(filename)
            

def main():
    my_library = Library.load('lib.pckl')
    
    while True:
        newbook = Book()
        newbook.title = input('enter title: ').strip()
        newbook.author = input('enter author: ').strip()
        
        my_library.add_book(newbook)
        my_library.save()
        if input('continue? [y/n]').strip() == 'n':
            break
            
            
if __name__ == '__main__':
    main()

    
