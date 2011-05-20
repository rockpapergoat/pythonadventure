#!/usr/local/bin/python3.2
# 110508, add and remove books from a list
# 110519, move catalog to a global variable; dump on quit only

import pprint, pickle

catalog = {}


def add_books():
	"""method for adding books to a list"""
	'''title, author, pages, isbn, category'''
	entry = input('Give me some book details in this format: Title, Author, Pages, ISBN, Category\n')
	if len(entry) != 0:
		newbook = (entry.split(','))
		details = ['title','author','pages','isbn','category']
		catalog.update(dict(zip(details,newbook)))
		library = open('books.txt','ab')
		#pickle.dump(catalog,library)
		library.close()
	else:
		print('You need to pass me a book.')
		
def show_books():
	library = open('books.txt','rb')
	print('Here\'s your library:\n')
	catalog = pickle.load(library)
	#pprint.pprint(catalog)
	print(catalog)
	library.close

def remove_book():
	library = open('books.txt','wb')
	
	
def menu():
	answer = input('\n--------------------------\nWhat would you like to do?\n--------------------------\n1. Add books\n2. Remove books\n3. View all books\n4. Quit\n\n')
	return answer.rstrip()


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
		show_books()
		menu()
	elif choice == '4':
		print('Thanks for playing. See you next time.')
		pickle.dump(catalog,library)
		loopcount = 1
		exit(0)
