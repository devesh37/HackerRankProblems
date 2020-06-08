#!/bin/python3
#Problem Link:https://www.hackerrank.com/challenges/delete-duplicate-value-nodes-from-a-sorted-linked-list/problem
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

# Complete the removeDuplicates function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def removeDuplicates(head):
    pre=head
    nxt=head.next
    if(nxt==None):
        return(head)
    while(nxt!=None):
        while(nxt!=None and pre.data==nxt.data):
            nxt=nxt.next
        if(nxt==None):
            pre.next=nxt
            break
        pre.next=nxt
        pre=nxt
        nxt=nxt.next
    return(head)



if __name__ == '__main__':