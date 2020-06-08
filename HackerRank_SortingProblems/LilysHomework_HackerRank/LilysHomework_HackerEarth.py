#!/bin/python3

import math
import os
import random
import re
import sys
from threading import Thread 
# Complete the lilysHomework function below.
#solving by graph approch
def lilysHomework(a,out,index):
    alen=len(a)
    #actual position
    apos=list(enumerate(a))
    apos.sort(key=lambda x:x[1])
    visited=[False]*alen
    i=0
    swap=0
    for i in range(alen):
        if visited[i] or apos[i][0]==i:
            continue
        cycle_size=0
        j=i
        while(not visited[j]):
            visited[j]=True
            j=apos[j][0] #the index element with which it is exchanged
            cycle_size+=1
        if cycle_size>0:
            swap+=(cycle_size-1)
    out[index]=swap
    return(swap)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input())
    out=[0]*2
    arr = list(map(int, input().rstrip().split()))
    t1=Thread(target=lilysHomework,args=(arr,out,0))
    t2=Thread(target=lilysHomework,args=(list(reversed(arr)),out,1)) 
    t1.start()
    t2.start()
    t1.join()
    desc=t2.join()
    result = min(out[0],out[1])
    fptr.write(str(result) + '\n')

    fptr.close()
