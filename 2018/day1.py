#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  9 11:41:20 2018
Advent of Code Challenge
Day 1

@author: mattdesaix
"""


#############################################################################
############################ Part 1 #########################################
#############################################################################
"""
Challenge Summary: From a list of positive and negative values, find what the total sum is.
"""

import pandas as pd
import time

data = pd.read_csv("input_day1.txt", header = None)
data_list = data[0].tolist()

tmp = 497
for index, row in data.iterrows():
    tmp += row[0]
print("The sum of the frequnencies is %(freq)d" %{"freq": tmp })


#############################################################################
############################ Part 2 #########################################
#############################################################################
"""
Challenge Summary: Find which of the 'frequencies' is the first to occur twice (starting from 0).
For example: in [+1, -2, +4, -6, +2, +10], 
0 + 1 = 1,
1 - 2 = -1,
-1 + 4 = 3,
3 - 6 = -3,
-3 + 2 = -1 ...second instance of -1, thus -1 would be the answer
Note: it may take multiple iterations through a list to find the second frequency

This can take a long time, see DRASTIC differences below
"""

"""
2a) Slow and brutish
"""
x = [0]
tmp = 0
while True:
    for index, row in data.iterrows():
        tmp += row[0]
        if tmp in x:
            print("First frequency twice is %(freq2)d" %{"freq2": tmp} )
            break
        else: 
            x.extend([tmp])
    else:
        continue
    break
# Answer is 558 but algorithm is waaaay too slow

"""
2b) Faster! Use sets
"""



x = {0}
tmp = 0
start_time = time.time()
while True:
    for index, row in data.iterrows(): # iterates through pandas df
        tmp += row[0]
        if tmp in x:
            print("First frequency twice is %(freq2)d" %{"freq2": tmp} )
            print("That took %s seconds" % (time.time() - start_time))
            break
        else: 
            x.add(tmp)
    else:
        continue
    break
# 18.5 seconds

"""
1b) Fastest!! Use sets and
    ITERATE THROUGH A LIST, NOT A DATAFRAME
"""

x = {0}
tmp = 0
start_time = time.time()
while True:
    for row in data_list: # iterates through data as list
        tmp += row
        if tmp in x:
            print("First frequency twice is %(freq2)d" %{"freq2": tmp} )
            print("That took %s seconds" % (time.time() - start_time))
            break
        else: 
            x.add(tmp)
    else:
        continue
    break
## 0.13327 seconds
    



