#!/bin/usr/python

import csv
import sys

def add_to_list(l,iterator,date,is_new,zone):
    if not is_new:
        for y in l[iterator][1]:
            if y[0] == date.strip():
                y[1] = y[1] + 1
                return l
    else:
        new = initialize_new(zone)
        l.append(new)
        for y in l[iterator][1]:
            if str(y[0]) == date.strip():
                y[1] = y[1] + 1
                return l
    return l

def initialize_new(zone):
    new = [zone,[["2015-12-1",0]]]
    for i in range(2,11):
        mem = ["2015-12-" + str(i),0]
        new[1].append(mem)
    return new

def most_pickups(l):
    top_date = ""
    max_pickups = -1
    for y in l:
        if y[1] > max_pickups:
            top_date = y[0]
            max_pickups = y[1]
    return [top_date,max_pickups]

def reduce(f):
    l = []
    csv_reader = csv.reader(f)
    iterator = -1
    curr_zone = -1
    for line in csv_reader:
        if curr_zone == int(line[0]):
            l = add_to_list(l,iterator,line[1],False,curr_zone)
        else:
            curr_zone = int(line[0])
            iterator = iterator + 1
            l = add_to_list(l,iterator,line[1],True,curr_zone)

    for x in l:
        new = most_pickups(x[1])
        x[1] = new
    for x in l:
        x = str(x)
        x = x.replace('[','')
        x = x.replace(']','')
        print x
def main():
    reduce(sys.stdin)

if __name__ == "__main__":
    main()





