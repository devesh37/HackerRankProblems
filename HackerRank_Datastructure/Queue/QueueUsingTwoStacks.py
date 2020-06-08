#!/bin/python3

import math
import os
import random
import re
import sys
class Queue:
    def __init__(self):
        self.queue=list()
    def enque(self,x):
        self.queue.append(x)
    def deque(self):
        if(self.queue):
            return(self.queue.pop(0))
        else:
            return("")
    def peek(self):
        if(self.queue):
            return(self.queue[0])
        else:
            return("")
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    t = int(input())
    q=Queue()
    for t_itr in range(t):
        inp=input().split()
        op=int(inp[0])
        if(op==1):
            q.enque(int(inp[1]))
        elif(op==2):
            q.deque()
        else:
            fptr.write(str(q.peek())+"\n")
    fptr.close()
