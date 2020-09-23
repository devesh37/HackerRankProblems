#Link: https://www.hackerrank.com/challenges/ctci-array-left-rotation/problem
#!/bin/python3
import math
import os
import random
import re
import sys
# Complete the rotLeft function below.
def rotLeft(a, d):
    alen=len(a)
    i=0
    b=list()
    while(i<alen):
        newindex=((i+d)%alen)
        b.append(a[newindex])
        i+=1
    return(b)
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    nd = input().split()
    n = int(nd[0])
    d = int(nd[1])
    a = list(map(int, input().rstrip().split()))
    result = rotLeft(a, d)
    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')
    fptr.close()
