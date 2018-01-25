#!/usr/bin/python

import sys
import string

with open(sys.argv[1],'rb') as air:
    lines=air.readlines()
    lines.pop(0)
    for l in lines:
        d = l.replace('"','')
        d = d.split(',')
            
        print d[0]
