#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the hackerlandRadioTransmitters function below.
def hackerlandRadioTransmitters(x, k):
    x.sort()
    xlen=len(x)
    i=0
    n=0
    while(i<xlen):
        n+=1
        pos=x[i]+k
        while(i<xlen and x[i]<=pos):
            i+=1
        i-=1
        pos=x[i]+k
        while(i<xlen and x[i]<=pos):
            i+=1
    return(n)
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    x = list(map(int, input().rstrip().split()))

    result = hackerlandRadioTransmitters(x, k)

    fptr.write(str(result) + '\n')

    fptr.close()
