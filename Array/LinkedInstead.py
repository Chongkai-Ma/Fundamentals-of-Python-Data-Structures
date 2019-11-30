#!/usr/bin/python3

from node import Node

head = None 

for count in range(1, 10):
    head = Node(count, head)

probe = head
targetItem = 5
while probe != None and targetItem != probe.data:
    probe = probe.next
if probe != None:
    probe.data = 88888
    print ("The item has been changed")
else:
    print ("The item has not been found")

