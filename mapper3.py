#!/usr/bin/python

import sys
import string

for line in sys.stdin:   
    d = line.replace('"','')
    d = d.split(',')
    print d[0]
