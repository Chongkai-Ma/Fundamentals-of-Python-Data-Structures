#!/usr/bin/python3

def test_stack():
    #create a list to emulate the stack
    s = []
    print ("now is a empty stack", s)
    s.append("a")
    print ("push a to the stack", s)
    s.append("b")
    print ("push b to the stack", s)
    s.append("c")
    print ("push c to the stack", s)
    Len = len(s)
    print ("The stack has ", Len, "items")
    s.pop()
    print ("remove the top item of the stack", s)
    s.pop()
    print ("remove the top item of the stack", s)
    s.pop()
    print ("remove the top item of the stack", s)
    s.append("d")
    print ("Add a new item to the stack", s)



print (test_stack())

