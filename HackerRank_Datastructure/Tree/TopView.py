#Problem Link:https://www.hackerrank.com/challenges/tree-top-view/problem
class Node:
    def __init__(self, info): 
        self.info = info  
        self.left = None  
        self.right = None 
        self.level = None 

    def __str__(self):
        return str(self.info) 

class BinarySearchTree:
    def __init__(self): 
        self.root = None

    def create(self, val):  
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root
         
            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break

"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.info (the value of the node)
"""
def levelOrderTraversal(root):
    tmp=root
    queue=list()
    queue.append(tmp)
    out=list()
    while(queue):
        node=queue.pop(0)
        out.append(node.info)
        if(node.left!=None):
           queue.append(node.left)
        if(node.right!=None):
            queue.append(node.right)
    return(out)

def HorizontalDistance(root):
    root.info=[root.info,0]
    hd=dict()
    temp=dict()
    hd[0]=[root.info[0]]
    queue=list()
    queue.append(root)
    while(queue):
        node=queue.pop(0)
        if(node.left!=None):
           queue.append(node.left)
           lhd=node.info[1]-1
           node.left.info=[node.left.info,lhd]
           if(lhd in hd):
                hd[lhd].append(node.left.info[0])
           else:
                hd[lhd]=[node.left.info[0]]
        if(node.right!=None):
           queue.append(node.right) 
           rhd=node.info[1]+1
           node.right.info=[node.right.info,rhd]
           if(rhd in hd):
                hd[rhd].append(node.right.info[0])
           else:
                hd[rhd]=[node.right.info[0]]
    
    for i in sorted(hd):
        temp[i]=hd[i]
    del hd
    return(temp)
    

def topView(root):
    if(root!=None):
        lo=levelOrderTraversal(root)
        hd=HorizontalDistance(root)
        for i in hd:
            if(len(hd[i])==1):
               print(hd[i][0],end=" ")
            else:
                mins=len(lo)
                item=None
                for j in hd[i]:
                    tmp=lo.index(j)
                    if(tmp<mins):
                        mins=tmp
                        item=j
                print(item,end=" ")
                    

        return
    
        


tree = BinarySearchTree()
t = int(input())

arr = list(map(int, input().split()))

for i in range(t):
    tree.create(arr[i])

topView(tree.root)