#!/bin/python3

import os
import sys
#https://www.hackerrank.com/challenges/and-xor-or/problem
def andXorOr(a):
    stack=list()
    maxs=0
    for i in a:
        while stack:
            top=stack[-1]
            s=i^top
            if(s>maxs):
                maxs=s
            if(i<top):
                stack.pop()
            else:
                break
        stack.append(i) 
    return(maxs)
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a_count = int(input())

    a = list(map(int, input().rstrip().split()))

    result = andXorOr(a)

    fptr.write(str(result) + '\n')

    fptr.close()
