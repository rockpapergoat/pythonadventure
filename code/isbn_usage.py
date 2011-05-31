#!/usr/local/bin/python3.2
# cf. http://wiki.pobblelabs.org/MakingLibrarySoftware5

import isbndb
from pprint import pprint

#book_data = isbndb.by_isbn('W8NQQ89H', '9781852332709')
# book_data acts like a list of results from isbndb.com.  you can
# get the first result with book_data[0]
# (there should be only 1 result for isbn queries)
#pprint(book_data[0])

book_data = isbndb.by_title('W8NQQ89H', '"learning python"')
# notice the double quotes around the title.
# that lets you search for an exact match (as far as I can tell).
for book in book_data:
    pprint(book)
