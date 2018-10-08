#!/usr/bin/python
import sys

current_key = None
previous_key = None
current_sum = 0

for line in sys.stdin:
    line = line.strip()
    line = line.split("\t")
    
    key,value = line[0],float(line[1])
    
    if key == current_key:
        current_res += value
        previous_key = key
    else:
        if current_key:
            to_print = '({}),{}'.format(previous_key, current_res)
            print(to_print)
            previous_key = None
        current_key = key
        previous_key = key
        current_res = value
to_print = '({}),{}'.format(current_key, current_res)
print(to_print)