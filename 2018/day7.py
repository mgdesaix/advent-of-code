#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 12 21:15:59 2018
Advent of Code Challenge
Day 7
@author: mattdesaix
"""

import numpy as np
import pandas as pd
import time

data = pd.read_csv("./input_day7.txt", header = None)
data[0].str.split(' ').tolist()[0][1]
full_instruct = np.chararray(shape = (len(data), 2))
for i in range(len(data)):
    before = data[0].str.split(' ').tolist()[i][1]
    after = data[0].str.split(' ').tolist()[i][7]
    full_instruct[i][0] = before
    full_instruct[i][1] = after
    

instruct = np.array([['C', 'A'],
                      ['C', 'F'],
                      ['A', 'B'],
                      ['A', 'D'],
                      ['B', 'E'],
                      ['D', 'E'],
                      ['F', 'E']])


def findStart (instructionArray):
    uniqueStarts = np.unique(instructionArray[:,[0]])
    uniqueEnds = np.unique(instructionArray[:,[1]])
    starts = []
    for start in uniqueStarts:
        if start not in uniqueEnds:
            starts.append(start)
    return sorted(starts)

def findNext (startDict):
    for instruction in sorted(startDict):
        if len(startDict[instruction]) == 0:
            return instruction

def addDependencies(nextLetter, instructionArray, startDict, instructionOrder):
    dependencyList = np.ndarray.tolist(instructionArray[instructionArray[:,0] == nextLetter][:,1])    
    for dependency in dependencyList:
        dependencies = np.ndarray.tolist(instructionArray[instructionArray[:,1] == dependency][:,0])
        startDict[dependency] = []
        if len(dependencies) > 1:
            dependencies.remove(nextLetter)
            for i in dependencies:
                if i not in instructionOrder:
                    startDict[dependency].append(i)
    return startDict       

def orderInstructions (instructionArray):
    start_time = time.time()
    listOfStarts = findStart(instructionArray)
    startDict = {}
    for start in listOfStarts:
        startDict[start] = []
    
    instructionOrder = []
    
    while len(startDict) > 0:
        nextLetter = findNext(startDict)
        startDict = addDependencies(nextLetter, instructionArray, startDict, instructionOrder)
        instructionOrder.append(nextLetter)
        startDict.pop(nextLetter)
    
    final_time = time.time() - start_time
    print('That took {} sec'.format(final_time))
    final_order = ''.join(instructionOrder)
    
    return final_order

orderInstructions(instruct)

orderInstructions(full_instruct)

#############################################################################
############################ Part 2 #########################################
#############################################################################
"""
Challenge Summary:  
"""
from collections import Counter


def workerQueue(startDict, workers, deltaT, queueOrder):
    
    for letter in sorted(startDict):
        if len(startDict[letter]) == 0 and letter not in queueOrder:
            duration = ord(letter) - ord('A') + deltaT
            queueOrder[letter] = duration
            if len(queueOrder) == workers:
                break;
    return queueOrder
  
      
def queueTime(queueOrderOld, workerTime):
    subtractCounter = Counter()
    minimum = min(queueOrderOld.values())
    for letter in queueOrderOld:
        subtractCounter[letter] = minimum
    queueOrderOld.subtract(subtractCounter)
    workerTime += minimum
    nextLetter = min(sorted(queueOrderOld), key = queueOrderOld.get)
    del queueOrderOld[nextLetter]
    return (queueOrderOld, workerTime, nextLetter)

def orderInstructions2( instructionArray, workers, deltaT):
    start_time = time.time()
    workerTime = 0
    listOfStarts = findStart(instructionArray)
    startDict = {}
    for start in listOfStarts:
        startDict[start] = []
        
    instructionOrder = []
    queueOrder = Counter()
    
    while len(startDict) > 0:
        queueOrder = workerQueue(startDict, workers, deltaT, queueOrder)
        queueOrder, workerTime, nextLetter = queueTime(queueOrder, workerTime)
        startDict = addDependencies(nextLetter, instructionArray, startDict, instructionOrder)
        instructionOrder.append(nextLetter)
        startDict.pop(nextLetter)
    final_time = time.time() - start_time
    print('That took {} Elves {} sec to complete the instructions'.format(workers, workerTime))
    final_order = ''.join(instructionOrder)
    final_time = time.time() - start_time
    print('That took {} sec for the computer to process'.format(final_time))
    return final_order

orderInstructions2(instruct, 2, 1)


orderInstructions2(full_instruct, 5, 61)

