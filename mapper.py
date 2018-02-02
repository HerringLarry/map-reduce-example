#!/usr/bin/python

import csv
import sys
import string

def mapper():
    """
        Reads in csv from system,
    enters it as an argument
    in the csv.reader() function
    and parses it. Eventually it outputs
    the [zone, date]. Outputs to 
    bash command sort.
    """

    data = sys.stdin.readlines()
    reader = csv.reader(data,delimiter = ',')
    reader.next() #skips header, for some reason header is not already skipped
    for line in reader:
        if int(line[21]) > 100 and int(line[21]) <= 200: # if zone is between 100 and 200
                #sys.stdout.write([line[21] +',' + line[3] + ',' + '\n'])  #Zone and date, counts as one pickup
                
                print line[21] +',' +  line[3]

def main():
    mapper()
    
if __name__ == '__main__':
    main()

