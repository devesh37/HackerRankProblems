#!/bin/python3

import math
import os
import random
import re
import sys

def poisonousPlants(p):
    stack = []
    mDays = -math.inf

    for plant in p:
        days = 1
        while stack and stack[-1][0] >= plant:
            _, d = stack.pop()
            days = max(days, d + 1)
        if not stack:
            days = 0
        mDays = max(mDays, days)
        stack.append((plant, days))
    
    return mDays




if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    p = list(map(int, input().rstrip().split()))

    result = poisonousPlants(p)

    fptr.write(str(result) + '\n')

    fptr.close()
1