#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  9 15:00:09 2018
Advent of Code Challenge
Day 2
@author: mattdesaix
"""

#############################################################################
############################ Part 1 #########################################
#############################################################################
"""
Challenge Summary: From numerous strings, find how many have an instance of
a letter twice (but not every instance within that string, i.e. 'ababcd' counts once, not twice)
and the instance of a letter three times.  Return the product of these two values
"""
import pandas as pd
import time

## In this list, there are 4 strings with letters found twice, and
## 3 strings with letters found 3 times.
# thus the checksum is 12
my_list = ["abcdef", "bababc", "abbcde", "abcccd", "aabcdd", "abcdee", "ababab"]

            
def getChecksum(stringList):
    start_time = time.time()
    doubles = 0
    triples = 0
    for string in stringList:
        letter_set = {}
        for letter in string:
            if letter in letter_set:
                letter_set[letter] += 1
            else:
                letter_set[letter] = 1
        values = letter_set.values()
        if 2 in values:
            doubles += 1
        if 3 in values:
            triples += 1
    checksum = doubles * triples
    print("There are {} doubles and {} triples".format(doubles, triples))
    print("The checksum is {}".format(checksum))
    total_time = time.time() - start_time
    print("That took %s seconds" % total_time)
    return

getChecksum(my_list)



"""
Now for the real test
1a)
"""

day2 = pd.read_csv("./input_day2.txt", header = None)
day2.head()
day2 = day2[0].tolist()

getChecksum(day2)




#############################################################################
############################ Part 2 #########################################
#############################################################################
"""
Challenge Summary: Find the two strings from the input that differ by only one character,
then return all of the characters except the differing one.
"""

def findIDs(stringList):
    start_time = time.time()
    for x in range(0, len(stringList)-1): # iterate string 1
        for y in range(x, len(stringList)): #iterate string 2
            count = 0
            for z in range(0, len(stringList[x])): # iterates the letters of the strings
                if stringList[x][z] != stringList[y][z]:
                    outOfPlace = z
                    count += 1 # keeps count of how many differences b/n the two strings
                    if count == 2: # once it surpasses one difference, break.
                        break
            if count == 1: # if it gets through the strings and there's only one difference then end
                print("The two strings are: ")
                print(stringList[x])
                print(stringList[y])
                total_time = time.time() - start_time
                theString = list(stringList[x])
                theString.pop(outOfPlace)
                print("The final string is: ")
                print("".join(theString))
                print("That took %s seconds" % total_time)
                break
        else:
            continue
        break
    return
findIDs(day2)









