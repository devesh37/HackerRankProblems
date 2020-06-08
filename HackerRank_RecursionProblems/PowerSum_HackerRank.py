#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the powerSum function below.
def powerSum(X,N,i):
    if((i**N)<X):
        return powerSum(X,N,i+1)+powerSum(X-(i**N),N,i+1)
    elif((i**N)==X):
        return(1)
    else:
        return(0)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    X = int(input())

    N = int(input())

    result = powerSum(X,N,1)
    fptr.write(str(result) + '\n')

    fptr.close()
