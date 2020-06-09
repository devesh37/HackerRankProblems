#!/bin/python3

import os
import sys

#
# Complete the equalStacks function below.
#
def equalStacks(h1, h2, h3,s1,s2,s3,small):
    while((h1) and (h2) and (h3)):
        if(small!=s1):
            temp=h1.pop(0)
            s1-=temp
            if(small>s1):
                small=s1
        if(small!=s2):
            temp=h2.pop(0)
            s2-=temp
            if(small>s2):
                small=s2
        if(small!=s3):
            temp=h3.pop(0)
            s3-=temp
            if(small>s3):
                small=s3
        if(s1==s2 and s2==s3):
            return(s1)
    return(0)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    small=0
    
    n1N2N3 = input().split()

    n1 = int(n1N2N3[0])

    n2 = int(n1N2N3[1])

    n3 = int(n1N2N3[2])

    h1 = list(map(int, input().rstrip().split()))
    small=sum1=sum(h1)
    h2 = list(map(int, input().rstrip().split()))
    sum2=sum(h2)
    if(sum2<small):
        small=sum2
    h3 = list(map(int, input().rstrip().split()))
    sum3=sum(h3)
    if(sum3<small):
        small=sum3
    result = equalStacks(h1, h2, h3,sum1,sum2,sum3,small)
    fptr.write(str(result) + '\n')
    fptr.close()
