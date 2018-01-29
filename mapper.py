#!/usr/bin/python

import csv
import sys
import string

def mapper(file_name):
    with open(file_name,'r') as f:
        reader = csv.reader(f)
        reader.next() #skip header
        for line in reader:
            if int(line[21]) < 100:
                sys.stdout.write(line[21] + ', ' + line[3] +  '\n')  #Zone and amount of pickups  which will always be 1


def main():
    mapper(sys.argv[1])
    
if __name__ == '__main__':
    main()

