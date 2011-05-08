#!/usr/local/bin/python3.2
# 110506, Write a program to add and remove books from a list. Share and discuss.

'''
outline

- set up a dictionary with this form: {author: "first, last", title: "title", pages: number, ISBN: number, category: "genre"}
- accept either stdin or a file (csv?)
- add each line to the dict
- add methods to add, remove, find books
- add usage and menu

'''


catalog = []


def usage():
	"""print usage"""
	pass

def menu():
	answer = input('\n--------------------------\nWhat would you like to do?\n--------------------------\n1. Add books\n2. Remove books\n3. Search for books\n4. Edit an entry\n5. Quit\n\n')
	return answer.rstrip()

def add_books():
	"""method for adding books to a list"""
	'''title, author, pages, isbn, category'''
	entry = input('Give me some book details in this format: Title, Author, Pages, ISBN, Category\n')
	if len(entry) != 0:
		print(entry.split(','))
	else:
		print('You need to pass me a book.')
	pass

def append_item():
	"""append parameters to already entered records"""
	pass

def remove_books():
	pass

def find_books():
	"""method to look up books in catalog"""
	pass


	
"""present a menu to choose tasks"""
choice = menu()
if choice == '1':
	add_books()
elif choice == '2':
	print("Yo, this isn't working yet.")
elif choice == '3':
	print("Yo, this isn't working yet.")
elif choice == '4':
	print("Yo, this isn't working yet.")
elif choice == '5':
	print('Thanks for playing. See you next time.')
	exit(0)