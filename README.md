# Fundamentals-of-Python-Data-Structures

**ARRAY**.

Array is sequence that can be viewed and insteaded by index. An array is like a list in the python, but the client can use only [], len, iter(for) and str. The basic level of list is array. We use the list to study the Array. In the array, coder can not add in or delete the elementes. However, the we can use some algorithm to achieve those function. 

In the memory, the array is saved in a continuous address. 

                         Machine Address                       array                    index
                                                        -----------------                          
                             10011101                   |               |                  0
                                                        -----------------
                                                        -----------------
                             10011110                   |               |                  1
                                                        -----------------
                                                        -----------------
                             10011111                   |               |                  2
                                                        -----------------
                                                        -----------------
                             10100000                   |               |                  3
                                                        -----------------
                                                        -----------------
                             10100001                   |               |                  4
                                                        -----------------

When python want to get the array, there are two steps:
        1. Get the machine address firstly.
        2. Add the index for the machine address then return the result.


**LINKED**

Linked structure include single linked structure and doubly linked structure. It is samiliar with array; however, array is consequent in the memory while linked is not. Linked use pointer to indicate next data.  

   head |   --|-->  | D1 |  --|-->  | D2 |  --|--> | D3 | \ |                    single linked structure
   
   head |   --|-->  | \ |D1 |  <--|----|-->  | D2 |  <--|----|-->  | D3 | \ |    Double linked structure

Linked structure can add or delete element in the link and this active does not need to use axera memory. Coders can select different structure to finish different function. 


**STACK**

Python does not have internal function to finish the stack. Thus, we can use array (list) to emulate the stack to finish the stack's functions. The stack is **last-in First-out**. There are some operations of stack.

             Operation           Status              Return               comments
         s = <Stack Type>()                                            Start a stack, empty stack
         s.push(a)                 a                                   Stack have first element "a" 
         s.push(b)                 a b                                 "b" is the top element in the stack
         s.push(c)                 a b c                               "c" is the top element in the stack
         s.isEmpty()               a b c              False            The stack is not empty
         len(s)                    a b c                3              There are three elements i the stack
         s.peek()                  a b c                c              reture the top element but not to delete it
         s.pop()                   a b                  c              reture the top element and delete it
         s.pop()                   a                    b              return the top element and delete it
         s.pop()                                        a              return the top element and delete it
         s.isEmpty()                                   True            Now it is empty stack
         s.peek()                                      KeyError        call a empty stack is an error
         s.pop()                                       keyError        delete a empty stack is an error
         s.push(d)                 d                                   Now d is the top element


**QUEUE**

Python does not have internal function to finish the queue. Thus, we can use array (list) to emulate the queue to finish the queue's functions. The queue is **First-in First-out**. There are some operations of queue.

             Operation           Status              Return               comments
         q = <Queue Type>()                                            Start a queue, empoty queue
         q.add(a)                  a                                   The queue involve first element "a"
         q.add(b)                  a b                                 "a" is the first element, "b" is last element
         q.add(c)                  a b c                               "c" is the first element
         q.isEmpty                 a b c               False           The queue is not empty
         len(q)                    a b c                 3             The queue include 3 elements
         q.peek()                  a b c                 a             return the first element but not to delete it
         q.pop()                   b c                   a             return the first element and delete it
         q.pop()                   c                     b             returm the first element and delete it
         q.pop()                                         c             return the first element and delete it
         q.isEmpty()                                   True            Now the queue is empty
         q.peek()                                      error           call a empty queue is an error
         q.pop()                                       error           delete a empty queue is an error
         q.add(d)                  d                                   "d" is the first element is the queue


**LIST**

List is the last liner set. It has more functions than stack and queue have. It can add elements at anywhere, any time. There are two types of list options. The first one is base on index operation. The second one is base on content. 

There are some operations based on index.

               Method                                              Result
         L.insert(i, item)                                   Add a item at index i
         L.pop(i = None)                                     return and delete index i 
         L.[i]                                               Return the item at index i
         L.[i] = item                                        Use item instead of item i
        

There are some operations based on item.

               Method                                              Result
         L.append(item)                                      Add a item as end of list
         L.remove(item)                                      del item in the list
         L.index(item)                                       return the index of the item. 

