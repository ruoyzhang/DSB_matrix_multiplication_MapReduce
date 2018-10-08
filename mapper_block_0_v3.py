#!/usr/bin/python
import sys
import numpy as np
m = int(sys.argv[1])
n = int(sys.argv[2])
p = int(sys.argv[3])

height = int(sys.argv[4])
width = int(sys.argv[5])



for line in sys.stdin:
    
    line = line.strip()
    
    #split the line by comma and form a list
    line_l = line.split(",")
    
    row, col, value = int(line_l[1]), int(line_l[2]), float(line_l[3])

    #treating entries from A
    if (line_l[0] == "A"):

        #dividing the matrix A into blocks of size height x width and assigning the entry a block index
        block_ind_i = int((row) / height)    #this requires us to select appropriate block size
        block_ind_j = int((col) / width)      #otherwise this assign mechanism may fail in cases where size is too smal in comp with m and p (rounding error)

        #each block is duplicated 1 + int(p / width) times
        for dup_ind in range(1 + int((p - 1) / height)):
            #key = block_ind_i, block_ind_j, block_ind_p
            to_print = '{0:d},{1:d},{2:d}\tA,{3:d},{4:d},{5:f}'.format(block_ind_i, block_ind_j, dup_ind, row, col, value)
            print(to_print)

    #treating entries from B
    else:
        block_ind_j = int((row) / width)
        block_ind_p = int((col) / height)
        # each block is duplicated 1 + int(m / height) times
        for dup_ind in range(1 + int((m - 1) / height)):
            #key = block_ind_i, block_ind_j, block_ind_p
            #notice the block index puts the column index first
            to_print = '{0:d},{1:d},{2:d}\tB,{3:d},{4:d},{5:f}'.format(dup_ind, block_ind_j, block_ind_p, row, col, value)
            print(to_print)