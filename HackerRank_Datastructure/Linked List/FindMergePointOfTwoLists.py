#!/bin/python3
#Problem Link: https://www.hackerrank.com/challenges/find-the-merge-point-of-two-joined-linked-lists/problem
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

# Complete the findMergeNode function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def findMergeNode(head1, head2):
    t1=head1
    t2=head2
    c1=0
    c2=0
    i=0
    while(t1!=None):
        c1+=1
        t1=t1.next
    while(t2!=None):
        c2+=1
        t2=t2.next
    t1=head1
    t2=head2
    if(c1>c2):
       while(i<(c1-c2)):
        t1=t1.next
        i+=1
       while(t1!=t2):
            t1=t1.next
            t2=t2.next
       return(t1.data)
    else:
       while(i<(c2-c1)):
           t2=t2.next
           i+=1
       while(t1!=t2):
            t1=t1.next
            t2=t2.next
       return(t1.data)

if __name__ == '__main__':