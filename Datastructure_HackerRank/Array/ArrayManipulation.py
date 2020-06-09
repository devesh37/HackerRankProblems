#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the arrayManipulation function below.
def arrayManipulation(n, queries):
    array=[0]*(n)
    maximum=0
    temp=0
    for q in queries:
        i=q[0]-1
        j=q[1]-1
        temp=q[2]
        array[i]+=temp
        if((j+1)<n):
            array[j+1]-=temp
    temp=0
    for i in range(0,n):
        temp=temp+array[i]
        if(maximum<temp):
            maximum=temp
    return(maximum)
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)

    fptr.write(str(result) + '\n')

    fptr.close()
