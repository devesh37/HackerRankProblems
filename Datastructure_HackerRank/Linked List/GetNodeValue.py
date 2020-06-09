#!/bin/python3
#Problem link:https://www.hackerrank.com/challenges/get-the-value-of-the-node-at-a-specific-position-from-the-tail/problem
import math
import os
import random
import re
import sys

class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = SinglyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node


        self.tail = node

def print_singly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))

        node = node.next

        if node:
            fptr.write(sep)

# Complete the getNode function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def getNode(head, pos):
    temp=head
    t=-1
    while(temp!=None):
        if(pos==0 and temp.next==None):
            return(temp.data)
        t+=1
        temp=temp.next
    temp=head
    fpos=0
    while(True):
        if(t-fpos==pos):
            return(temp.data)
        fpos+=1
        temp=temp.next
      


if __name__ == '__main__':