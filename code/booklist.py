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

def usage():
	"""print usage"""
	print('The menu describes usage. Please type a number.')
	

def menu():
	answer = input('\n--------------------------\nWhat would you like to do?\n--------------------------\n1. Add books\n2. Remove books\n3. Search for books\n4. Edit an entry\n5. View all books\n6. Quit\n\n')
	return answer.rstrip()

def add_books():
	"""method for adding books to a list"""
	'''title, author, pages, isbn, category'''
	entry = input('Give me some book details in this format: Title, Author, Pages, ISBN, Category\n')
	if len(entry) != 0:
		newbook = (entry.split(','))
		details = ['title','author','pages','isbn','category']
		catalog.update(dict(zip(details,newbook)))
		print(catalog)
	else:
		print('You need to  me a book.')


def append_item():
	"""append parameters to already entered records"""
	

def remove_books():
	'''method to remove books from catalog dict'''

def show_catalog():
	"""show what's in the catalog now"""
	print('Your catalog includes:\n')
	#for (key,value) in catalog:
	#	print(catalog[key,value])
	print(sorted(catalog))

def find_books():
	"""method to look up books in catalog"""
	

def not_working():
	"""output something in place of methods that don't exist yet"""
	print("Yo, this isn't working yet.")
	

	
"""present a menu to choose tasks"""

catalog = {}
loopcount = 0
while loopcount == 0:
	choice = menu()
	if choice == '1':
		add_books()
		menu()
	elif choice == '2':
		not_working()
		menu()
	elif choice == '3':
		not_working()
		menu()
	elif choice == '4':
		not_working()
		menu()
	elif choice == '5':
		show_catalog()
		menu()
	elif choice == '6':
		print('Thanks for playing. See you next time.')
		loopcount = 1
		exit(0)
	else:
		usage()
		menu()