#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  9 23:39:43 2018
Advent of Code Challenge
Day 4
@author: mattdesaix
"""

#############################################################################
############################ Part 1 #########################################
#############################################################################
"""
Challenge Summary: The input data has a time stamped events (though unsorted) of guard activity.
Sort the data by time and find which guard slept the most and at what minute.
"""
import pandas as pd
import time

data = pd.read_csv("./input_day4.txt", header = None)
newDF = pd.DataFrame(columns = ["date", "string", "guard"])
newDF["date"] = pd.to_datetime(data[0].str[6:17], format = "%m-%d %H:%M")
newDF["string"] = pd.DataFrame(data[0].str.split('] ', 1).tolist())[1]
newDF = newDF.sort_values("date").reset_index(drop = True)

"""
1a) Find the sleepiest guard and his sleepiest minute
"""

def SleepyGuard(newDF):
    start_time = time.time()
    guardDict = {}
    maxSleep = newDF['date'][0] - newDF['date'][0]
    for x in range(len(newDF)): # this finds the sleepiest guard
        if "Guard" in newDF['string'][x]: # check if 'guard' is in string value
            guard = newDF['string'][x].split(' ')[1] # if so, save guard id
        if "wakes" in newDF['string'][x]: # wakes always follows sleeps, if 'wakes' in string calculate time asleep
            delta = newDF['date'][x] - newDF['date'][x-1]
            if guard in guardDict:
                guardDict[guard] += delta # add time to dict if guard already in there
            else:
                guardDict[guard] = delta
            if guardDict[guard] >= maxSleep:
                    maxSleep = guardDict[guard]
                    sleepyGuard = guard
    print("The sleepiest guard is {} with {} sleep".format(sleepyGuard, maxSleep))
    
    minuteDict = {}
    for x in range(60): # creates dictionary for minute values
        minuteDict[x] = 0
    for x in range(len(newDF)):
        if "Guard" in newDF['string'][x]:
            guard = newDF['string'][x].split(' ')[1]
        if "wakes" in newDF['string'][x] and guard == sleepyGuard:
            delta = newDF['date'][x] - newDF['date'][x-1]
            minutes = delta.seconds/60
            for y in range(minutes):
                minuteDict[ (newDF['date'][x-1].minute + y) % 60] += 1
    minuteMax = max(minuteDict, key = minuteDict.get)
    print("His sleepiest minute is {}".format(minuteMax))
    idXmin = int(sleepyGuard[1:]) * minuteMax
    print("Guard ID times sleepiest minute is {}".format(idXmin))
    total_time = time.time() - start_time
    print("That took {} seconds to complete".format(total_time))
    return;

SleepyGuard(newDF)



#############################################################################
############################ Part 2 #########################################
#############################################################################
"""
Challenge Summary: Find at what minute a guard was sleeping the most,
and identify the specific guard.
"""

def SleepyMinute(newDF):
    start_time = time.time()
    fullDict = {}
    for x in range(len(newDF)): # this finds the sleepiest guard
        if "Guard" in newDF['string'][x]: # check if 'guard' is in string value
            guard = newDF['string'][x].split(' ')[1] # if so, save guard id
        if "wakes" in newDF['string'][x]: # wakes always follows sleeps, if 'wakes' in string calculate time asleep
            delta = newDF['date'][x] - newDF['date'][x-1]
            minutes = delta.seconds/60
            if guard not in fullDict:
                fullDict[guard] = {}
                for y in range(60):
                    fullDict[guard][y] = 0
            for z in range(minutes):
                minute = (newDF['date'][x-1].minute + z) % 60
                fullDict[guard][minute] += 1
    max_value = 0
    for key in fullDict:
        this_max_value = max(fullDict[key].values())
        if this_max_value > max_value:
            max_guard = key
            max_key = max(fullDict[key], key = fullDict[key].get)
            max_value = this_max_value
        
        
    # sleepyMinuteGuard = max(fullDict, key = fullDict.get)
    print("The guard asleep on the same minute the most is guard {}".format(max_guard))
    # sleepiestMinute = max(fullDict[sleepyMinuteGuard], key = fullDict[sleepyMinuteGuard].get)
    print("The guard's sleepiest minute is {}".format(max_key))
    idXmin = int(max_guard[1:]) * max_key
    print("Guard ID times sleepiest minute is {}".format(idXmin))
    total_time = time.time() - start_time
    print("That took {} seconds to complete".format(total_time))
    return fullDict;

d = SleepyMinute(newDF)









