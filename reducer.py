#!/bin/usr/python

import csv
import sys

def add_to_list(l,it,date,is_new,zone):
    """
        If new zone has not been reached by the it
    then the function adds one to the cumulative total 
    of the corresponding date in the list. 
    
        If new zone had been reached then initializes
    a list that will eventually be outputted, appends it to
    list l, and add one to the cumulative total of the 
    corresponding date in the list
    """
    if not is_new: 
        for y in l[it][1]: #iterates through dates [135,[<<<<"2015-12-3">>>>,1]] indicated by pointed brackets
            print y
            print y[0]
            if str(y[0]) == date.strip():
                y[1] = y[1] + 1 #adds one to corresponding date's cumulative total
                return l
    else:
        new = initialize_new(zone) #initializes new list because zone is not in l
        l.append(new)
        for y in l[it][1]:
            if str(y[0]) == date.strip():
                y[1] = y[1] + 1
                return l
    return l

def initialize_new(zone):
    """
        Creates list consisting of 
    the zone number and the date and 
    initialized, cumulative pickup total.
    """
        
    new = [zone,[["2015-12-1",0]]] #Begins at "2015-12-1" 
    for i in range(2,11):
        mem = ["2015-12-" + str(i),0] #Creates nine more consecutive members
        new[1].append(mem)
    return new

def most_pickups(l):
    """
        Finds the date on which the most pickups
    happened and returns that date and it's 
    cumulative pickups
    """
    top_date = ""
    max_pickups = -1
    for y in l:
        if y[1] > max_pickups:
            top_date = y[0] #sets top date
            max_pickups = y[1] #sets max pickups
    return [top_date,max_pickups] #Returns list

def reduce(f):
    """
        Parse input and inputs each row into 
    add_to_list function to be processed. 
    Eventually creates list with [zone,[date,max_pickups] 
    format. Eventually outputs newly created list
    """
    l = []
    csv_reader = csv.reader(f)
    it = -1
    curr_zone = -1
    for line in csv_reader:
        new_zone = int(line[0])
        if curr_zone == new_zone: #checks zone against 
            l = add_to_list(l,it,line[1],False,curr_zone) #False indicates not new zone
        else:
            curr_zone = new_zone
            it = it + 1
            l = add_to_list(l,it,line[1],True,curr_zone)

    for x in l:
        new = most_pickups(x[1]) #Finds max_pickups
        x[1] = new
    for x in l:
        x = str(x)
        x = x.replace('[','') #Cleans output
        x = x.replace(']','')
        x = x.replace('\'','')
        print x


def main():
    reduce(sys.stdin)

if __name__ == "__main__":
    main()





