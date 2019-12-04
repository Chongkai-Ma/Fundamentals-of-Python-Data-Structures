#!/usr/bin/python3

def test_queue():
    #using a list to create queue
    q = []
    print ("Now is a empty queue", q)
    q.append("a")
    print ("Add a new item in the list", q)
    q.append("b")
    print ("Add a new item in the list", q)
    q.append("c")
    print ("Add a new item in the list", q)
    LEN = len(q)
    print ("There are ", LEN, "items in the queue")
    q.pop(0)
    print ("Now we delete first item in the queue", q)
    q.pop(0)
    print ("Now we delete next item in the queue", q)
    q.pop(0)
    print ("Now we delete last item in the queue", q)
    q.append("d")
    print ("Now we can add another one in the queue", q)

print (test_queue())

