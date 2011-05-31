#!/usr/local/bin/python3.2
# 110506, Write a program to add and remove books from a list. Share and discuss.
# 110526, 
"""
outline

- set up a dictionary with this form: {timestamp: timestamp, author: "first, last", title: "title", pages: "number", ISBN: "number", genre: "genre"}
- accept either stdin or a file (csv?)
- add each line to the dict
- add methods to add, remove, find books
- add usage and menu

"""

import shelve
import time
import pprint
import cmd
import os.path

class Book:
	def __init__(self):
		"""
		books have these attributes:
			timestamp
			title
			author
			pages
			isbn
			genre
		all are strings.
		"""
		self.timestamp = ''
		self.title = ''
		self.author = ''
		self.pages = ''
		self.isbn = ''
		self.genre = ''

class Library:
	"""
	methods dealing with library manipulation
	"""
	
	def Keys(self, Keys):
		"""set up some Keys"""
		Keys = ['timestamp', 'title', 'author', 'pages', 'isbn', 'genre']
	
	
	def load(database):
		if os.path.exists(database):
			shelve.open(database)
		else:
			# if it doesn't exist, create a new instance of the library
			shelve.open(database)

	def save(database):
		"""
		close the db
		"""
		close(database)


	def add_book(self, database, book):
		"""
		data should be a dictionary.
		there's no type checking here. just format as a dict.
		{title:, author:, pages:, isbn:, genre:}
		"""
		timestamp = str(int(time.time()))
		print(timestamp)
		if book:
			database[Book.timestamp] = book
			print(book)
			

	def show_all_records(self, database):
		"""show what's in the catalog now"""
		print('Your library includes:\n')
		dvals = list(database.values())
		print(sorted(dvals))
	
	def append_item(self, database, title):
		"""append parameters to already entered records"""
	
	def remove_book(self, database, title):
		"""method to remove books from catalog dict"""

	def find_book(self, database, title):
		"""method to find a book from catalog dict"""
		#found = 


def not_working():
	"""output something in place of methods that don't exist yet"""
	print("Yo, this isn't working yet.")
	


class Menu(cmd.Cmd):
	prompt = '::> '

	def __init__(self):
		cmd.Cmd.__init__(self)

		library_filename = 'library'
		self.library = Library.load(library_filename)

	def do_add(self, arg):
		"""
		add a book
		"""
		newbook = Book()
		newbook.title = input("Enter book title: ").strip()
		newbook.author = input("Enter book author: ").strip()
		self.library.add_book(newbook)

	def do_l(self, arg):
		"""
		list the books
		"""
		print('here are all my books:')
		for book in self.library.get_all_books():
		    print("{} by {}".format(book.title, book.author))
	do_list = do_l

	def do_q(self, arg):
		"""
		quit
		"""
		self.library.save()
		print('saved.')
		print('bye!')
		return True
	do_EOF = do_quit = do_q

my_menu = Menu()
my_menu.cmdloop('\nWelcome to the library\n')