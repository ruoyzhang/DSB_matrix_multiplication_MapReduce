#!/usr/bin/python
import sys
import numpy as np
current_key = None
current_res = 0
A_block_entries, B_block_entries = dict(), dict()
i_scale, j_scale, p_scale = 0, 0, 0
height = int(sys.argv[1])
width = int(sys.argv[2])

def BlockResults(current_key, A_block_entries, B_block_entries):
    
    a_block, b_block, c_block = current_key[0], current_key[1], current_key[2]
    min_i = height * a_block # the range of index which involving calculation
    max_i = min(height * (a_block + 1) - 1, i_scale)
    min_j = width * b_block 
    max_j = min(width * (b_block + 1) - 1, j_scale)
    min_p = height * c_block
    max_p = min(height * (c_block + 1) - 1, p_scale)
    #compute/output result
    for i1 in range(max_i - min_i + 1):
        for k1 in range(max_p - min_p + 1):
            i = min_i + i1
            k = min_p + k1
            current_res = 0
            for j in range(max_j - min_j + 1):
                try:
                    current_res += A_block_entries[i][min_j+j] * B_block_entries[min_j+j][k]
                except KeyError:
                    pass
            print('{0:d},{1:d}\t{2:f}'.format(i, k, current_res))
                
def DataStorageA(matrix, row, col, A_block_entries, i_scale, j_scale):
    if row not in A_block_entries:
        A_block_entries[row] = dict()
    A_block_entries[row][col] = val
    i_scale = max(i_scale, row) # range of index
    j_scale = max(j_scale, col)
    return A_block_entries, i_scale, j_scale

def DataStorageB(matrix, row, col, B_block_entries, p_scale):
    if row not in B_block_entries:
        B_block_entries[row] = dict()
    B_block_entries[row][col] = val
    p_scale = max(p_scale, col) # range of index
    return B_block_entries, p_scale

for line in sys.stdin:
    
    line = line.strip()
    key, line = line.split("\t")
    key = tuple(map(int, key.split(",")))
    value = line.split(",")
    which_matrix = value[0]
    row, col, val = int(value[1]),int(value[2]),float(value[3])
    
    #if we're still on the same key
    if key == current_key:
        #then we store the entries into a block
        if which_matrix == "A":
            A_block_entries, i_scale, j_scale = DataStorageA(which_matrix, row, col, A_block_entries, i_scale, j_scale)
        else:
            B_block_entries, p_scale = DataStorageB(which_matrix, row, col, B_block_entries, p_scale)
    
    #otherwise: 2 scenarios:
    #I. the first key we're seeing: we set current_key and store values into blocks
    #II. we're onto a new key: we calculate the block results and flush the results out, then set new current key
    else:
        #this is scenario II --> flushing results out
        if current_key:
            #print("*******RESULTS CALCULATION******")
            BlockResults(current_key, A_block_entries, B_block_entries)
        
        #set new key
        current_key = key
        #reset result holder
        current_res = 0
        #reset block scale variables
        i_scale, j_scale, p_scale = 0,0,0
        #reset blocks
        A_block_entries, B_block_entries = dict(),dict()
        
        #store entries
        if which_matrix == "A":
            A_block_entries, i_scale, j_scale = DataStorageA(which_matrix, row, col, A_block_entries, i_scale, j_scale)
        else:
            B_block_entries, p_scale = DataStorageB(which_matrix, row, col, B_block_entries, p_scale)
if current_key:
    BlockResults(current_key, A_block_entries, B_block_entries)