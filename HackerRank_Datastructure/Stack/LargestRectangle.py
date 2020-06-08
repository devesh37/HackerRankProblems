#!/bin/python3
import math
import os
import random
import re
import sys
# Complete the largestRectangle function below.
def largestRectangle(h):
    i=0
    hlen=len(h)
    area=0
    while(i<hlen):
        j=i-1
        l=i+1
        height=h[i]
        k=1
        while(j>=0 and height<=h[j]):
            k+=1
            j-=1
        while(l<hlen and height<=h[l]):     
            k+=1
            l+=1
        A=k*height
        if(A>area):
            area=A
        i+=1
    return(area)
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    h = list(map(int, input().rstrip().split()))

    result = largestRectangle(h)

    fptr.write(str(result) + '\n')

    fptr.close()
