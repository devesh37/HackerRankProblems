#ProblemLink: https://www.hackerrank.com/challenges/swap-nodes-algo/problem
#!/bin/python3
import os
import sys
sys.setrecursionlimit(10**6)
class Node:
    def __init__(self, info):
        self.info = info  
        self.left = None  
        self.right = None 
        self.level = None 
    def __str__(self):
        return str(self.info)
class BinaryTree:
    def __init__(self,root):
        self.root=root
    def insertLeft(self,node):
        self.root.left=node
    def insertRight(self,node):
        self.root.right=node

def inOrder(root,arr):
    if root == None:
        return
    inOrder(root.left,arr)
    arr.append(root.info)
    inOrder(root.right,arr)
def func(bt, queries):
    out=[]
    h=height(bt.root)
    for k in queries:
           m=1
           tmp=list()
           while((m*k)<=h):
                swapNode(bt.root,m*k,1)
                m+=1
           inOrder(bt.root,tmp)
           out.append(tmp)
    return(out)

           
def height(root):
    if((root==None) or(root.left==None and root.right==None)):
        return(0)
    else:
        h=max(height(root.left),height(root.right))
        return(h+1)

def swapNode(node,k,d):
        if(node==None):
            return
        if(k==d):
            node.left,node.right=node.right,node.left
            return
        swapNode(node.left,k,d+1)
        swapNode(node.right,k,d+1)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())
    bt=BinaryTree(Node(1))
    queue=list()
    queue.append(bt.root)
    indexes = [1]
    for _ in range(n):
        if(not queue):
            continue
        node=queue.pop(0)
        tmp=(list(map(int, input().rstrip().split())))
        l=tmp[0]
        r=tmp[1]
        if(l!=-1):
            node.left=Node(l)
            queue.append(node.left)
        if(r!=-1):
            node.right=Node(r)
            queue.append(node.right)
    queries_count = int(input())
    queries = []
    for _ in range(queries_count):
        queries_item = int(input())
        queries.append(queries_item)
    l=list()
    inOrder(bt.root,l)
    result = func(bt, queries)
    for k in result:
        for i in k:
            fptr.write(str(i)+" ")
        fptr.write('\n')
    fptr.close()