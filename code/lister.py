#!/usr/local/bin/python3.2

'''
add, remove books from a list.
this doesn't store the data anywhere static.
'''

def add_thing():
   item = input("please give me a book record to add.\n")
   if len(item) != 0:
     ALIST.append(item)
     print("here's your list:\n")
     print(ALIST)
   elif len(item) == 0:
     print("try again")

def remove_thing():
  print("here's your list now.\n")
  print(ALIST)
  item_index = input("what do you want to delete?\ntype an index number:")
  ALIST.pop(int(item_index))
  print("here's your list:\n")
  print(ALIST)

ALIST = []
while True:
    choice = input("choose one of these:\n1. add\n2. remove\n")
    if choice.__contains__('1'):
        add_thing()
    if choice.__contains__('2'):
        remove_thing()


