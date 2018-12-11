#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  9 20:19:52 2018
Advent of Code Challenge
Day 3
@author: mattdesaix
"""

#############################################################################
############################ Part 1 #########################################
#############################################################################
"""
Challenge Summary: Given the coordinates for a large number of grids with unique IDs:
1) Find how many cells from across all the grids are overlapping. 
2) Find which grid is not overlapping any others
"""
import pandas as pd
import numpy as np
import time

## Practice

leftTest = [1, 3, 5]
topTest = [3, 1, 5]
rowTest = [4, 4, 2]
colTest = [4, 4, 2]

def FillArray(left, top, row, col):
    a = np.zeros(shape = (1000,1000))
    for x in range(len(left)):
        a[top[x]:top[x]+row[x], left[x]:left[x]+col[x]] += 1
    overlap = np.sum(a >= 2)
    print("The number of overlapping cells is {}".format(overlap))
    return;
FillArray(leftTest, topTest, rowTest, colTest)

"""
Goals 1 and 2 are completed by the following function, FillandFind()
"""


data = pd.read_csv("./input_day3.txt", header = None, sep = " ")
data.head()

def FillandFind(messyDF):
    start_time = time.time()
    """ 
    Retrieve the pieces of information needed from the character string
    left -> indentation from left
    top -> indentation from top
    col -> number of columns
    row -> number of rows
    """
    left = pd.DataFrame(messyDF[2].str.split(',',0).tolist())[0].tolist()
    left = map(int, left)
    top = pd.DataFrame(messyDF[2].str.split(',',0).tolist())[1].str.rstrip(':').tolist()
    top = map(int, top)
    col = pd.DataFrame(messyDF[3].str.split('x',0).tolist())[0].tolist()
    col = map(int, col)
    row = pd.DataFrame(messyDF[3].str.split('x',0).tolist())[1].tolist()
    row = map(int, row)
    
    a = np.zeros(shape = (1000, 1000)) #these values seem to encompass the entire area neededv
    for x in range(len(messyDF)):
        a[top[x]:top[x]+row[x], left[x]:left[x]+col[x]] += 1
    overlap = np.sum(a >= 2)
    print("The number of overlapping cells is {}".format(overlap))
    total_time = time.time() - start_time
    print("That took %s seconds" % total_time)
    
    for x in range(len(messyDF)):
        if np.sum(a[top[x]:top[x]+row[x], left[x]:left[x]+col[x]]) == row[x] * col[x]:
            print("The non-overlapping segment is {}".format(data[0][x]))
            break
    return;

FillandFind(data)
