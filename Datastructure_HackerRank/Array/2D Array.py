#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the hourglassSum function below.
#it has some debug output
def hourglassSum(a):
    i=0
    sums=None
    while(i<4):
        j=0
        print("i=",i)
        while(j<4):
            temp0=a[i][j:j+3]
            temp1=a[i+1][j:j+3][1]
            temp2=a[i+2][j:j+3]
            tempsum=sum(temp0)+sum(temp2)+temp1
            if(sums==None):
                sums=tempsum
            elif(tempsum>sums):
                sums=tempsum
            print("-------------------")
            print(temp0)
            print("  ",temp1," ")
            print(temp2)
            print("Sums=",tempsum)
            j+=1
        print('_')
        i+=1
    return(sums)

    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
