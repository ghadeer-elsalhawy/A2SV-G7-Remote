#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#
def printList(arr):
    for i in range(len(arr)):
        if i == len(arr) - 1:
            print(arr[i])
        else:
            print(arr[i], end=" ")
def insertionSort1(n, arr):
    to_place = arr[-1]
    status = False
 
    for i in range(n - 2, -1, -1):
        if arr[i] > to_place:
            arr[i + 1] = arr[i]
            printList(arr) 
        else:
            arr[i + 1] = to_place
            status = True
            break
    if not status:
        arr[0] = to_place
    printList(arr)
    
        

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
