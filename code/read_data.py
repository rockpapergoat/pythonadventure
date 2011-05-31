#!/usr/local/bin/python3.2
# 110530, 
import shelve
import isbndb

def read_data(filename):
     keys = ('isbn','title','author')
     n = open('output.txt','w')
     f = open(filename)
     for line in f:
          n.write(str(dict(zip(keys,line.rstrip().split('\t')))))
     f.close()
     n.close()

#DB = shelve.open('databword')

read_data('titles.txt')