#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the insertionSort function below.

def mergeSort(a,left,right):
    shift=0
    if(left<right):
        mid=left+int((right-left)/2)
        shift+=mergeSort(a,left,mid)
        shift+=mergeSort(a,mid+1,right)
        shift+=join(a,left,mid+1,right)
    return(shift)
def join(a,left,mid,right):
    i=left
    j=mid
    temp=list()
    shift=0
    while(i<mid and j<=right):
        if(a[i]<=a[j]):
            temp.append(a[i])
            i+=1
        else:
            shift+=(mid-i)
            temp.append(a[j])
            j+=1
    while(i<mid):
        temp.append(a[i])
        i+=1
    while(j<=right):
        temp.append(a[j])
        j+=1
    k=0
    while(left<=right):
        a[left]=temp[k]
        k+=1
        left+=1    
    return(shift)    


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())
        arr = list(map(int, input().rstrip().split()))
        result=mergeSort(arr,0,(n-1))
        fptr.write(str(result) + '\n')

    fptr.close()
