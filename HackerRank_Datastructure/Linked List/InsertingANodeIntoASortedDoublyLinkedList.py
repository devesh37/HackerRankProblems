#!/bin/python3
#ProblemLink: https://www.hackerrank.com/challenges/insert-a-node-into-a-sorted-doubly-linked-list/problem
import math
import os
import random
import re
import sys

class DoublyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = DoublyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node
            node.prev = self.tail


        self.tail = node

def print_doubly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))

        node = node.next

        if node:
            fptr.write(sep)

# Complete the sortedInsert function below.

#
# For your reference:
#
# DoublyLinkedListNode:
#     int data
#     DoublyLinkedListNode next
#     DoublyLinkedListNode prev
#
#
def sortedInsert(head, data):
    n=head
    p=None
    newNode=DoublyLinkedListNode(data)
    while(n!=None and n.data<data):
        p=n
        n=n.next
    newNode.next=n
    if(n==None):
        p.next=newNode
        newNode.prev=p
        return(head)
    if(n==head):
        newNode.prev=None
        n.prev=newNode
        head=newNode
        return(head)
    newNode.prev=n.prev
    n.prev.next=newNode
    n.prev=newNode
    return(head)


if __name__ == '__main__':