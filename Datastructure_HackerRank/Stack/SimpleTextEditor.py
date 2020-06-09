import math
import os
import random
import re
import sys
#problem link:
#https://www.hackerrank.com/challenges/simple-text-editor/problem?h_r=next-challenge&h_v=zen
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    stack=list()
    str1=str()
    Q= int(input())
    i=0
    while i < Q:
        inp = list(input().rstrip().split())
        q=int(inp[0])
        if(q==1):
            stack.append([1,len(inp[1])])
            str1=str1+inp[1]
        elif(q==2):
            delete=int(inp[1])
            l=len(str1)
            stack.append([q,str1[(l-delete):l]])
            str1=str1[0:(l-delete)]
        elif(q==3):
            k=int(inp[1])-1
            fptr.write(str1[k]+ '\n')
        else:
            undo=stack.pop()
            if(undo[0]==1):
                str1=str1[0:len(str1)-undo[1]]
            else:
                str1=str1+undo[1]

        i+=1  

    fptr.close()
