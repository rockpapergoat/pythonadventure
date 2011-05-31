'''isbndb: Queries isbndb.com for metadata about books

To Use:
(go to isbndb.com, sign up, and get an access key)
searching by title:
>>> q = isbndb.Query('YOUR KEY YERE', title='"Stumbling on Happiness"')
>>> q[0]
{'publisher': 'New York : Alfred A. Knopf, c2006.', 'isbn': '1400042666', 'author': 'Daniel Gilbert', 'notes': 'Includes bibliographical references (p. 239-268) and index.', 'title': 'Stumbling on happiness', 'title_long': None, 'summary': "Why are lovers quicker to forgive their partners for infidelity than for leaving dirty dishes in the sink? Why do patients remember long medical procedures as less painful than short ones? Why do home sellers demand prices they wouldn't dream of paying if they were home buyers? Why does the line at the grocery store always slow down when we join it? In this book, Harvard psychologist Gilbert describes the foibles of imagination and illusions of foresight that cause each of us to misconceive our tomorrows and misestimate our satisfactions. Using the latest research in psychology, cognitive neuroscience, philosophy, and behavioral economics, Gilbert reveals what we have discovered about the uniquely human ability to imagine the future, our capacity to predict how much we will like it when we get there, and why we seem to know so little about the hearts and minds of the people we are about to become.--From publisher description."}
>>> len(q)
8

searching by ISBN #:
>>> q = isbndb.Query('YOUR KEY HERE', isbn='9780262012706')
>>> q[0]
{'publisher': 'Cambridge, Mass. : The MIT Press, c2009.', 'isbn': '0262012707', 'author': 'Sherry Turkle; with additional essays by William J. Clancey... [et al.]', 'notes': 'Includes bibliographical references and index.\n\nSimulation and its discontents /Sherry Turkle --What does simulation want? --Theview from the 1980s --design and science at the millennium --New ways of knowing/New ways of forgetting --Sites of simulation: case studies --Outer space and undersea --Becoming a rover /William J. ClanceyIntimate sensing /Stefan Helmreich --Buildings and biology --Performing the protein fold /Natasha Myers.', 'title': 'Simulation and its discontents', 'title_long': None, 'summary': None}

Copyright 2011 Dave St.Germain
'''
import urllib.request, urllib.parse
from xml.etree import ElementTree

class NotFoundException(Exception):
    pass

class Query:
    SERVER_URL = 'http://isbndb.com/api/books.xml'
    
    def __init__(self, access_key, isbn='', title=''):
        self.access_key = access_key
        self.isbn = isbn
        self.title = title
        self.responses = []
        self.books = []
        self.total = 0
        self.limit = 100
    
    def __getitem__(self, idx):
        if not self.responses:
            self._run()
        return self.books[idx]
    
    def __len__(self):
        return len(self.books)
    
    def __repr__(self):
        return 'Query({!r}, title={!r}, isbn={!r}) -> {!r}'.format(self.access_key, self.title, self.isbn, self.books)
        
    def __iter__(self):
        if not self.responses:
            self._run()
        return iter(self.books)
        
    def _run(self, pagenum=1):
        pars = {'access_key': self.access_key,
                'results': 'texts',
                'page_number': pagenum,
        }
        if self.isbn:
            pars['index1'] = 'isbn'
            pars['value1'] = self.isbn
        elif self.title:
            pars['index1'] = 'title'
            pars['value1'] = self.title
        else:
            raise Exception('title or isbn required')
        qs = urllib.parse.urlencode(pars)
        url = '{}?{}'.format(self.SERVER_URL, qs)
        with urllib.request.urlopen(url) as fp:
            data = fp.read()

        tree = ElementTree.fromstring(data)
        if not self.responses:
            self.total = int(tree.find('./BookList').get('total_results'))
            if self.total == 0:
                raise NotFoundException()
                
        self.responses.append(tree)
        for b in tree.find('./BookList'):
            book = {
                'title': b.find('Title').text,
                'title_long': b.find('TitleLong').text,
                'author': b.find('AuthorsText').text,
                'summary': b.find('Summary').text,
                'isbn': b.get('isbn'),
                'publisher': b.find('PublisherText').text,
                'notes': b.find('Notes').text
            }
            self.books.append(book)
        while self.total > len(self.books) and len(self.books) <= self.limit:
            self._run(pagenum+1)
                


def by_title(api_key, title):
    """
    shortcut to query by title
    """
    return Query(api_key, title=title)

def by_isbn(api_key, isbn):
    """
    shortcut to query by isbn
    """
    return Query(api_key, isbn=isbn)

    
    