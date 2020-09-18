#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 18 00:52:00 2020

@author: niscowal
"""


import numpy as np
import random

arr = np.zeros([4,4])

def init(array):
    col = random.randint(0, 3)
    row = random.randint(0,3)
    if(array[row,col] == 0):
        array[row,col] = 2
        print(array)
        print("")
        direction = input("Enter direction:")
        move(direction, array)
    else:
        init(array)
    
    
def move(action, initial_array):
        temp_array = initial_array.copy()
        if(action.lower() not in ["left", "right", "up", "down"]):
            new_direction = input("Enter a left, right, up, or down:")
            move(new_direction, initial_array)
        else:
            for row in range(0,4):
                temp_row = []
                for col in range(0,4):
                    if(action.lower() == "left" or action.lower() == "right"):
                        if(initial_array[row,col] > 0):
                            if(len(temp_row) != 0 and temp_row[len(temp_row)-1] == initial_array[row,col]):
                                temp_row[len(temp_row)-1] = initial_array[row,col]*2
                            else:
                                temp_row.append(initial_array[row,col]);
                    elif(action.lower() == "up" or action.lower() == "down"):
                        if(initial_array[col,row] > 0):
                            if(len(temp_row) != 0 and temp_row[len(temp_row)-1] == initial_array[col,row]):
                                temp_row[len(temp_row)-1] = initial_array[col,row]*2
                            else:
                                temp_row.append(initial_array[col,row]);
                if(action.lower() == "left"):
                    insert_row = np.pad(temp_row, (0,4-len(temp_row)), 'constant')
                    temp_array[row] = insert_row
                elif(action.lower() == "right"):
                    insert_row = np.pad(temp_row, (4-len(temp_row),0), 'constant')
                    temp_array[row] = insert_row
                if(action.lower() == "up"):
                    insert_row = np.pad(temp_row, (0,4-len(temp_row)), 'constant')
                    for row_num in range(0,4):
                        temp_array[row_num, row] = insert_row[row_num]
                elif(action.lower() == "down"):
                    insert_row = np.pad(temp_row, (4-len(temp_row),0), 'constant')
                    for row_num in range(0,4):
                        temp_array[row_num, row] = insert_row[row_num]
            if(np.array_equiv(initial_array,temp_array) == True):
                new_direction = input("Enter a different direction:")
                move(new_direction, initial_array)
            else:
                init(temp_array)

init(arr)
