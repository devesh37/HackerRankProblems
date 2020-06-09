#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the quickSort function below.
#def quickSort(arr):
def Partition(a,p,q):
    pivot=a[p]
    j=q
    i=q+1
    while(j>p):
        if(pivot<a[j]):
            i-=1
            a[i],a[j]=a[j],a[i]
        j-=1
    
    a[i-1],a[p]=a[p],a[i-1]
    return(a)    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = Partition(arr,0,len(arr)-1)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
