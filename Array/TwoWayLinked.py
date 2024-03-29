#!/usr/bin/python3

from TwoWayNode import TwoWayNode

#create a doubly linked structure with one node
head = TwoWayNode(1)
tail = head

#add four node to the end of the doubly linked structure
for data in range(2, 6):
    tail.next = TwoWayNode(data, tail)
    tail = tail.next

#print the contents of the linked structure in reverse order
probe = tail
while probe != None:
    print(probe.data)
    probe = probe.previous


