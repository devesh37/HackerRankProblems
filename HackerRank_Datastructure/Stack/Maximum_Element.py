#!/bin/python3
import math
import os
import random
import re
import sys
class Stack:
    def __init__(self):
        self.array=list()
        self.maximum=None
        self.top=-1
    def push(self,x):
        self.top+=1
        if(self.maximum==None):
            self.maximum=x
        elif(self.maximum<x):
            self.maximum=x
        self.array.append(x)
        
    def pop(self):
        temp=self.array[self.top]
        if(self.top!=-1):
            self.array.pop()
            self.top-=1
        if(self.top==-1):
            self.maximum=None
        if(temp==self.maximum and self.top!=-1):
            self.maximum=max(self.array)
            #print("Max:",self.maximum)
        return(temp)
    def maxi(self):
        return(self.maximum)
s=Stack()
N=int(input())
for i in range(N):
    q=list(map(int, input().rstrip().split()))
    #print(s.array)
    if(q[0]==1):
        s.push(q[1])
        continue
    if(q[0]==2):
        s.pop()
        continue
    print(s.maxi())
