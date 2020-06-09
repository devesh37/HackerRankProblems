#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countSort function below.
def countSort(arr):
    arrlen=len(arr)
    firsthalf=int(arrlen/2)
    countingArray=list()
    j=0
    for i in range(0,100):
        countingArray.append(list())
    for i in arr:
        index=int(i[0])
        element=None
        if(j<firsthalf):
            element="-"
        else:
            element=i[1]
        countingArray[index].append(element)
        j+=1
    for i in countingArray:
        for j in i:
            print(j,end=' ')
   
if __name__ == '__main__':
    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(input().rstrip().split())

    countSort(arr)
