#ProblemLink:https://www.hackerrank.com/challenges/fraudulent-activity-notifications/problem
#!/bin/python3
import math
import os
import random
import re
import sys
import collections
# Complete the activityNotifications function below.
def activityNotifications(e, d):
    maximum=max(e)+1
    element_count=[0]*maximum
    q=collections.deque(list())
    elen=len(e)
    day=0
    notifications=0
    while(day<elen):
        if(day>=d):
            if(e[day]>=2*Median(element_count,d)):
                notifications+=1
            element_count[q.popleft()]-=1
        element_count[e[day]]+=1
        q.append(e[day])
        day+=1
    return(notifications)
#element_count is a counting sort list 
def Median(element_count,alen):
    low=0
    high=0
    d=alen//2
    traversed=element_count[0]
    i=1
    while(traversed<=d):
        high=i
        if traversed<d:
            low=i
        traversed+=element_count[i]
        i+=1
    if alen%2!=0:
        return high
    else:
        return((low+high)/2)
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    nd = input().split()
    n = int(nd[0])
    d = int(nd[1])
    expenditure = list(map(int, input().rstrip().split()))
    result = activityNotifications(expenditure, d)
    fptr.write(str(result) + '\n')
    fptr.close()
