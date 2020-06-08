#!/bin/python3

import os
import sys

#
# Complete the twoStacks function below.
#
def twoStacks(x, a, b):
    alen,blen,sums,i,j,count=len(a),len(b),0,0,0,0
    while(i<alen and sums+a[i]<=x):
        sums+=a[i]
        i+=1
    count=i
    while(j<blen and i>-1):
        sums+=b[j]
        j+=1
        while(sums>x and i>0):
            i-=1
            sums-=a[i]
        if(sums<=x and i+j>count):
            count=i+j
        
    return(count)       


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    g = int(input())

    for g_itr in range(g):
        nmx = input().split()

        n = int(nmx[0])

        m = int(nmx[1])

        x = int(nmx[2])

        a = list(map(int, input().rstrip().split()))

        b = list(map(int, input().rstrip().split()))

        result = twoStacks(x, a, b)

        fptr.write(str(result) + '\n')

    fptr.close()
