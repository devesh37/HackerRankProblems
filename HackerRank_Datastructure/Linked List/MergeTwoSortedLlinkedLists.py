#!/bin/python3
#Problem Link: https://www.hackerrank.com/challenges/merge-two-sorted-linked-lists/problem
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

# Complete the mergeLists function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def mergeLists(head1, head2):
    newList=SinglyLinkedList()
    tmp3=newList.head=SinglyLinkedListNode(0)
    tmp1=head1
    tmp2=head2
    data=0
    while(tmp1!=None and tmp2!=None):
        if(tmp1.data<tmp2.data):
            data=tmp1.data
            tmp1=tmp1.next
        else:
            data=tmp2.data
            tmp2=tmp2.next
        tmp3.next=SinglyLinkedListNode(data)
        tmp3=tmp3.next
    while(tmp1!=None):
        tmp3.next=SinglyLinkedListNode(tmp1.data)
        tmp3=tmp3.next
        tmp1=tmp1.next
    while(tmp2!=None):
        tmp3.next=SinglyLinkedListNode(tmp2.data)
        tmp3=tmp3.next
        tmp2=tmp2.next
    return(newList.head.next)



if __name__ == '__main__':