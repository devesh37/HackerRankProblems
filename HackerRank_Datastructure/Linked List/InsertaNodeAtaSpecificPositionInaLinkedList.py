#!/bin/python3

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

# Complete the insertNodeAtPosition function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#Link: https://www.hackerrank.com/challenges/insert-a-node-at-a-specific-position-in-a-linked-list/problem?h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen
#
def insertNodeAtPosition(head, data, position):
    count=1
    newNode=SinglyLinkedListNode(data)
    if(head==None):
        head=newNode
        return(head)
    temp=head
    while(temp.next!=None and position!=(count)):
        temp=temp.next
        count+=1
    if(temp.next!=None):
        temp1=temp.next
        temp.next=newNode
        newNode.next=temp1
    else:
        temp.next=newNode
    return(head)


if __name__ == '__main__':