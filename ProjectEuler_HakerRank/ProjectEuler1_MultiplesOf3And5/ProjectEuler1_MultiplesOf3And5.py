#Problem Link:https://www.hackerrank.com/contests/projecteuler/challenges/euler001/problem
import sys
t=int(input())
Nsum=lambda n:(n*(n+1))>>1;
for i in range(t):
    n =int(input())
    n -=1;
    m3=int(n/3);
    m5=int(n/5);
    m15=int(n/15);
    print(3*Nsum(m3) + 5*Nsum(m5) - 15*Nsum(m15));