#!/usr/local/bin/python3.2
'''
testing argparse for option parsing. apparently, optparse is deprecated as of 2.7 or something.
'''

import argparse

parser = argparse.ArgumentParser(description='Add, remove, edit, and search for books in your library')
parser.add_argument('-a', help='add a book')
print(parser.parse_args())