#!/bin/python3

import math
import os
import random
import re
import sys
maps={'}':'{',')':'(',']':'['}
pop=['}',']',')']
YES='YES'
NO='NO'
def isBalanced(s):
    sums=0
    slen=len(s)
    if(slen%2!=0):
        return('NO')
    temp=list()
    for i in s:
        if i not in pop:
            temp.append(i)
        else:
            if(not temp):
                return(NO)
            j=temp.pop()
            if(maps[i]!=j):
                print("Not Matched:",j,i)
                return(NO)
            print("Matched:",j,i)
    return(YES)
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    t = int(input())
    for t_itr in range(t):
        s = input()
        print("i:",t_itr)
        result=isBalanced(s)
        fptr.write(result+'\n')
    fptr.close()