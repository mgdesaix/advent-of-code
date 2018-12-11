#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 10 20:44:50 2018
Advent of Code Challenge
Day 5
@author: mattdesaix
"""

#############################################################################
############################ Part 1 #########################################
#############################################################################
"""
Challenge Summary: Take a string of characters and if a uppercase letter and lowercase
of the same type touch then they are to be removed (ex. 'bCaAd' becomes 'bCd' because ).
Continue and reevaluate until no more 'reactions' occur 
(e.g. 'bCaAcd' finalizes at 'bd', b/c removing 'aA' puts 'c' and 'C' into contact)  
"""

import time

file = open('input_day5.txt', 'r')
polymer = file.read().strip()
file.close()
    
"""
Method A
Brutish and slow (>100 seconds)
"""
test = 'dabAcCaCBAcCcaDA'                     

def checkPolymerA(polymer):
    start_time = time.time()
    i = 0
    while i < (len(polymer)-1):
        if polymer[i].upper() == polymer[i+1].upper() and polymer[i] != polymer[i+1]:
                polymer = polymer[:i] + polymer[i+2:]
                i =- 1
        i += 1
    print('The length of the polymer is {}'.format(len(polymer)))
    final_time = time.time() - start_time
    print('That took {} seconds to complete'.format(final_time))
    return

checkPolymerA(test)

"""
Method B
Fast (<1 second), break it up!
"""

def react(polymer):
    L = len(polymer)
    if L < 2: # nothing to react if less than 2
        return polymer
    elif L == 2: # if length 2, check to see if react conditions are met, return '' if so
        if polymer[0] != polymer[1] and polymer[0].upper() == polymer[1].upper():
            return ''
        else: # otherwise return the two elements that didn't react
            return polymer
    else:
        half = L // 2
        if polymer[half-1] != polymer[half] and polymer[half-1].upper() == polymer[half].upper():
            return combine(react(polymer[:half-1]), react(polymer[half+1:]))
        else:
            return combine(react(polymer[:half]), react(polymer[half:]))
        
def combine(a, b):
    if a == '' or b == '':
        return a + b
    elif a[-1] != b[0] and a[-1].upper() == b[0].upper():
        return combine(a[:-1], b[1:])
    else:
        return a + b

def checkPolymerB(polymer):
    start_time = time.time()
    final_polymer = react(polymer)
    final_time = time.time() - start_time
    print('The final polymer unit length is {}'.format(len(final_polymer)))
    print('That took {} sec'.format(final_time))
    
checkPolymerB(polymer)



#############################################################################
############################ Part 2 #########################################
#############################################################################
"""
Challenge Summary: Now see when a letter (upper and lowercase) is removed from the entire sequence,
what the length of the sequence is.  Do this for each letter and find which produces
the shortest length.
"""


import sys
# recursion limit error occured for me during this process
sys.getrecursionlimit() # mine was on 1000
sys.setrecursionlimit(2800) # change to sufficient quantity


def checkPolymer2(polymer): ## uses react() and combine() from above
    
    start_time = time.time()
    """ Iterate through alphabet range for each lower and uppercase (combined) letter """
    d = {}
    for alpha in range(26):
        letters = chr( ord('a') + alpha) + chr( ord('a') + alpha).upper() # create lower and uppercase letter combo
        new_poly = polymer.translate(None, ''.join(letters)) # remove the letters from the sequence
        polymer_length = len(react(new_poly))
        d[letters] = polymer_length
    
    min_key = min(d, key = d.get)
    min_val = d[min_key]
    print('Removing the letters {} created the smallest polymer'.format(min_key))
    print('This polymer had a length of {}'.format(min_val))

    final_time = time.time() - start_time
    # print('The final polymer unit length is {}'.format(len(final_polymer)))
    print('That took {} sec'.format(final_time))
checkPolymer2(polymer)


