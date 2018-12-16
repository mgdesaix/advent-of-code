#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 11 16:21:27 2018
Advent of Code Challenge
Day 6
@author: mattdesaix
"""


#############################################################################
############################ Part 1 #########################################
#############################################################################
"""
Challenge Summary:  
"""
import time
import numpy as np


"""
Method 1a) My first idea was to create a 'boundary' around the points, then, starting at each
    point, look right,left,top,down and see if that is also closest to the point, if so, add
    1 to grid size.  While doing so I had a second array that added a 1 if that location was 
    conclusively determined to be closest to a point yet.  If it had, then the search wouldn't
    search there.  I used this method successfully for a Percolation problem in Java but didn't work
    here.  I created point objects to keep track of grid size
"""

class Point:
    def __init__(self, initX, initY):
        self.x = initX
        self.y = initY
        self.gridSize = 0
    
    def __str__(self):
        return 'x = %f, y = %f' % (self.x, self.y)



def search(i, x, y, coordDict, percolatedArray):
    if x < 0 or x == coordDict['xmax']: return;
    if y < 0 or y == coordDict['ymax']: return;
    if percolatedArray[x][y] == 1: return;
    
    if isClosest(i, x, y, coordDict, percolatedArray):
        percolatedArray[x,y] = 1
        if x == 0 or y == 0 or x == coordDict['xmax']-1 or y == coordDict['ymax']-1:
            coordDict['Point'][i].gridSize = float('inf')
        else:
            coordDict['Point'][i].gridSize += 1
        search(i, x+1, y, coordDict, percolatedArray)
        search(i, x, y+1, coordDict, percolatedArray)
        search(i, x-1, y, coordDict, percolatedArray)
        search(i, x, y-1, coordDict, percolatedArray)
    else: 
        return;
    
    
def isClosest(i, x, y, coordDict, percolatedArray):
    min_i = distManhattan(coordDict['Point'][i].x, coordDict['Point'][i].y, x, y)
    tmp = float('inf')
    for j in range(i+1, len(coordDict['Point'])):
        distance = distManhattan(coordDict['Point'][j].x, coordDict['Point'][j].y, x, y)
        if distance < tmp:
            tmp = distance
    if min_i < tmp:
        return True
    elif min_i == tmp:
        percolatedArray[x,y] = 1
        return False
    else:
        return False
        
    
def distManhattan(x1, y1, x2, y2):
    xdiff = abs(x2 - x1)
    ydiff = abs(y2 - y1)
    dist = xdiff + ydiff
    return dist   

def gridProblem1a(coordinates):
    start_time = time.time()
    xmin = np.ndarray.min(coordinates[:, 0])
    xmax = np.ndarray.max(coordinates[:, 0])
    ymin = np.ndarray.min(coordinates[:, 1])
    ymax = np.ndarray.max(coordinates[:, 1])
    
    coordDict = {}
    coordDict['xmax'] = xmax - xmin + 1
    coordDict['ymax'] = ymax - ymin + 1
    
    xdiff = xmax - xmin + 1
    ydiff = ymax - ymin + 1
    percolatedArray = np.zeros(shape = (xdiff, ydiff))
    
    coordDict['Point'] = {}
    for i in range(len(coordinates)):
        x = coordinates[i][0] - xmin
        y = coordinates[i][1] - ymin
        coordDict['Point'][i] = Point(x, y)
        # percolatedArray[x][y] = 1
    
    for i in range(len(coordinates)):
        search(i, coordDict['Point'][i].x, coordDict['Point'][i].y, coordDict, percolatedArray)
    tmp = 0
    for i in range(len(coordinates)):
        if coordDict['Point'][i].gridSize > tmp and coordDict['Point'][i].gridSize < float('inf'):
            tmp = coordDict['Point'][i].gridSize
    print ("The max grid size is {}".format(tmp))
    final_time = time.time() - start_time
    print('That took {} sec'.format(final_time))
    
    return coordDict


coordinates = np.array([[1, 1],
                        [1, 6],
                        [8, 3],
                        [3, 4],
                        [5, 5],
                        [8, 9]])
# Works with test data
output = gridProblem1a(coordinates)

"""
Read in actual data, method 1 did not work.  Recursion limit reached, even when setting it high
"""

file = open('input_day6.txt', 'r')
data = file.read().strip()
file.close()

import pandas as pd
data = pd.read_csv('input_day6.txt', delimiter = '\n', header = None)
str(data[0][0]).split(', ')
    
full_coordinates = np.zeros(shape = (len(data), 2), dtype = np.int64)
for i in range(len(data)):
    x = int( str(data[0][i]).split(', ')[0] )
    y = int( str(data[0][i]).split(', ')[1] )
    full_coordinates[i][0] = x
    full_coordinates[i][1] = y




"""

Method 1b) Brute, search each point within the boundary
    
"""




def gridProblem1b(coordinates):
    start_time = time.time()
    xmin = np.ndarray.min(coordinates[:, 0])
    xmax = np.ndarray.max(coordinates[:, 0])
    ymin = np.ndarray.min(coordinates[:, 1])
    ymax = np.ndarray.max(coordinates[:, 1])
    xdiff = xmax - xmin + 1
    ydiff = ymax - ymin + 1
    
    coordDict = {}
    coordDict['xmax'] = xmax - xmin + 1
    coordDict['ymax'] = ymax - ymin + 1
    coordDict['Point'] = {}
    for i in range(len(coordinates)):
        x = coordinates[i][0] - xmin
        y = coordinates[i][1] - ymin
        coordDict['Point'][i] = Point(x, y)
        # percolatedArray[x][y] = 1
    for x in range(xdiff):
        for y in range(ydiff):
            isClosest1b(x, y, coordDict)
    tmp = 0
    for i in range(len(coordinates)):
        if coordDict['Point'][i].gridSize > tmp and coordDict['Point'][i].gridSize < float('inf'):
            tmp = coordDict['Point'][i].gridSize
    print ("The max grid size is {}".format(tmp))
    final_time = time.time() - start_time
    print('That took {} sec'.format(final_time))
    
    return


def isClosest1b(x, y, coordDict):
    tmp = {}
    tmp2 = {}
    tmp['id'] = float('inf')
    tmp2['id'] = float('inf')
    for i in range(len(coordDict['Point'])):
        distance = distManhattan(coordDict['Point'][i].x, coordDict['Point'][i].y, x, y)
        if distance < tmp:
            tmp = distance
            id1 = i
        elif distance == tmp:
            tmp2 = distance
    if tmp < tmp2:
        if x == 0 or y == 0 or x == coordDict['xmax']-1 or y == coordDict['ymax']-1:
            coordDict['Point'][id1].gridSize = float('inf')
        else:
            coordDict['Point'][id1].gridSize += 1
    return

gridProblem1b(full_coordinates)

# Works, but takes 12.5 seconds. 

#############################################################################
############################ Part 2 #########################################
#############################################################################


def gridProblem2(coordinates):
    start_time = time.time()
    xmin = np.ndarray.min(coordinates[:, 0])
    xmax = np.ndarray.max(coordinates[:, 0])
    ymin = np.ndarray.min(coordinates[:, 1])
    ymax = np.ndarray.max(coordinates[:, 1])
    xdiff = xmax - xmin + 1
    ydiff = ymax - ymin + 1
    
    coordDict = {}
    coordDict['xmax'] = xmax - xmin + 1
    coordDict['ymax'] = ymax - ymin + 1
    coordDict['Point'] = {}
    coordDict['GridSize'] = 0
    for i in range(len(coordinates)):
        x = coordinates[i][0] - xmin
        y = coordinates[i][1] - ymin
        coordDict['Point'][i] = Point(x, y)
        # percolatedArray[x][y] = 1
    for x in range(xdiff):
        for y in range(ydiff):
            isClosest2(x, y, coordDict)
    
    print ("The max grid size with distance less than 10000 is {}".format(coordDict['GridSize']))
    final_time = time.time() - start_time
    print('That took {} sec'.format(final_time))
    
    return


def isClosest2(x, y, coordDict):
    tmp = 0
    for i in range(len(coordDict['Point'])):
        distance = distManhattan(coordDict['Point'][i].x, coordDict['Point'][i].y, x, y)
        tmp += distance
        if tmp >= 10000:
            return
    coordDict['GridSize'] += 1
    return

gridProblem2(full_coordinates)






   
