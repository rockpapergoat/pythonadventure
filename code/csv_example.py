#!/usr/local/bin/python3.2
# cf. http://docs.python.org/library/csv.html#examples
import csv
with open('titles.txt', 'r') as f:
    reader = csv.reader(f, delimiter='\t')
    for row in reader:
        print(row)