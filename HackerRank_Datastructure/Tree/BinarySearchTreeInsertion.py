#Problem Link:https://www.hackerrank.com/challenges/binary-search-tree-insertion/problem
class Node:
    def __init__(self, info):
        self.info = info  
        self.left = None  
        self.right = None 
        self.level = None 

    def __str__(self):
        return str(self.info) 

def preOrder(root):
    if root == None:
        return
    print (root.info, end=" ")
    preOrder(root.left)
    preOrder(root.right)
    
class BinarySearchTree:
    def __init__(self): 
        self.root = None

#Node is defined as
#self.left (the left child of the node)
#self.right (the right child of the node)
#self.info (the value of the node)

    def insert(self, val):
        tmp=self.root
        newNode=Node(val)
        if(tmp==None):
            self.root=newNode
            return
        while(True):
            if(tmp.info>=val):
                if(tmp.left==None):
                    tmp.left=newNode
                    break
                else:
                    tmp=tmp.left
            else:
                if(tmp.right==None):
                    tmp.right=newNode
                    break
                else:
                    tmp=tmp.right



tree = BinarySearchTree()
t = int(input())

arr = list(map(int, input().split()))

for i in range(t):
    tree.insert(arr[i])

preOrder(tree.root)
