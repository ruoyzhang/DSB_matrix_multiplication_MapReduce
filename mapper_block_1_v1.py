#!/usr/bin/python
import sys


for line in sys.stdin:
    line = line.strip()
    line = line.split("\t")
    
    key,value = line[0],line[1]
    
    to_print = '{}\t{}'.format(key, value)
    print(to_print)