#!/usr/bin/python3

from node import Node

head = None

for count in range(1, 6):
    head = Node(count, head)

probe = head
while probe != None:
    print (probe.data)
    probe = probe.next

    
