#!/usr/bin/python3

from node import Node

head = None

for count in range(1, 10):
    head = Node(count, head)

probe = head
targetItem = 15

'''
There is a loop, if probe != None and targetItem != probe.data
This loop will continue going on. 
Until it meet the end of the link or meet the targetItem. 

If we find the targetItem and probe not at the end,
the target has been found. 

If we do not find the targetItem and probe at the end,
the target has not been found. 
'''

while probe != None and targetItem != probe.data:
    probe = probe.next

if probe != None:           
    print ("target has been found")
else:
    print ("target has not been found")


