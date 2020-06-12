#Problem Link :https://www.hackerrank.com/challenges/is-binary-search-tree/problem
""" Node is defined as
class node:
  def __init__(self, data):
      self.data = data
      self.left = None
      self.right = None
"""
def inOrderTraversal(root,arr):
    if(root):
        inOrderTraversal(root.left,arr)
        arr.append(root.data)
        inOrderTraversal(root.right,arr)
        
def check_binary_search_tree_(root):
    arr=list()
    inOrderTraversal(root,arr)
    i=1
    alen=len(arr) 
    while(i<alen):
        if(arr[i-1]>=arr[i]):
            return(False)
        i+=1
    return(True)