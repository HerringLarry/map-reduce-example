#!/usr/bin/python

import csv
import sys
import string

def mapper():
    data = sys.stdin.readlines()
    reader = csv.reader(data,delimiter = ',')
    reader.next()
    for line in reader:
        if int(line[21]) > 100 and int(line[21]) <= 200:
                sys.stdout.write(line[21] + ', ' + line[3] +  '\n')  #Zone and amount of pickups  which will always be 1


def main():
    mapper()
    
if __name__ == '__main__':
    main()

