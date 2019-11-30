#!/usr/bin/python3

#from node import Node          # From node package import class Node

class Node(object):
    """Represent a singly linked node."""

    def __init__(self, data, next = None):
        self.data = data
        self.next = next


head = None

for count in range(1, 6):
    head = Node(count, head)   #Instance of the class Node. 

while head != None:
    print (head.data)
    head = head.next           #This is the indicate variable.


