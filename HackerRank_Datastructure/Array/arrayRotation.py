#!/bin/python3

import math
import os
import random
import re
import sys
def left_rotation(a,n,r):
    array=[0]*n
    i=0
    while(i<n):
        array[(i+n-r)%n]=a[i]
        i+=1
    for i in array:
        print(i,end=' ')



if __name__ == '__main__':
    nd = input().split()

    n = int(nd[0])

    r = int(nd[1])

    a = list(map(int, input().rstrip().split()))
    left_rotation(a,n,r)