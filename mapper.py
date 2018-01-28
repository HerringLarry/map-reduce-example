#!/usr/bin/python

import csv
import sys
import string

def mapper(file_name):
    with open(file_name) as f:
        reader = csv.reader(f,delimiter = ',')
        reader.next() #skip header
        for line in reader:
            sys.stdout.write(line[21] + ',1' + '\n')  #Zone and amount of pickups  which will always be 1
            #print line[21] + ', 1'


def main():
    mapper(sys.argv[1])
    
if __name__ == '__main__':
    main()

