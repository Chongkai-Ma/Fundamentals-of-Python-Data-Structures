#!/usr/bin/python3

"""
An array is like a list, but the client can use 
only [], len, iter(for) and str. The basic level
of list is array. 

We use the list to study the Array. In the array, 
coder can not add in or delete the elementes. 
However, the we can use some algorithm to achieve 
those function. 

In python, theose algorithm are be packaged and 
there are all in the function. 
"""

First_List = ["Google", "Facebook", "AWS", "Apple"]
Second_List = ["4", "2", "1", "5", "3"]

def create_list():
    # we create the list which same with we create the array. 
    print ("Now we have fist list: ", First_List) 
    
print (create_list())

def take_one_element():
    # we create the list and call one element. 
    Take_List1_First_elemt = First_List[0]
    Take_List2_First3_elemt = Second_List[0:3]    
    print ("Take list1 first elemt is :", Take_List1_First_elemt)
    print ("Take list2 first3 elemts are: ", Take_List2_First3_elemt)

print (take_one_element())

def update_one_element():
    #update one element in the array (list)
    First_List[2] = "BaiDu"
    print ("Change AWS to BaiDu", First_List)

print (update_one_element())

def del_one_element():
    '''
    As usual, the array can not delete the element. 
    In python, however; we can internal functions. 
    Thus, the delete element can be achieved using
    'del' functions
    '''
    del First_List[1]
    print ("delete Facebook element: ", First_List)

print (del_one_element())

def list_symbol():
    '''
    There some symbol can be used in the list
    For example: "len", "+", "*", "in", "-" ":"
    '''

    Count_List_element = len(First_List)
    print ("Count how many elements in the first list(len): ", Count_List_element)
    Two_List_Plus = First_List + Second_List 
    print ("Two list plus is(+): ", Two_List_Plus)
    Doub_List = Second_List*2
    print ("Double list(*): ", Doub_List)
    List_After_Second_element = First_List[1:]
    print ("Show the list after second element[1:]:", List_After_Second_element)
    Last_second_element = First_List[-2]
    print ("Show the last second element:", Last_second_element)

print (list_symbol())

def list_function():
    '''
    There are some functions in the list
        len(list)
        max(list)
        min(list)
        list(seq)   
    '''
    Max_fun = max(First_List)
    print ("The max point in the first list is ", Max_fun)
    Min_fun = min(Second_List)
    print ("The min point in list2 is ", Min_fun)

def list_method():
    '''
    There are some method in the python package.
    list.append()  add obj in the end of a list.
    list.count()   count how many obj in the list.
    list.extend()  add another list after the first list.
    list.index()   out put the index of the subject.
    list.pop()     remove the subject and out put the value of the subject. 
    list.remove()  remove a first object in the list. 
    list.reverse()
    list.sort()
    '''
    First_List.append("RedHat")
    print ("Add Red Hat in the first list: ", First_List)
    How_Google = First_List.count("google")  
    print ("How many google in the first list: ", How_Google)
    First_List.extend(Second_List)
    print ("First_list add second list is: ", First_List)
    OutPut_AWS_index = First_List.index("Apple")
    print ("Output AWS index in the first list:", OutPut_AWS_index)
    First_List.pop(-3)
    print ("remove the last third element in the first list:", First_List)
    First_List.remove("Google")
    print ("remove the google in the list: ", First_List)
    Second_List.reverse()
    print ("reverse second list: ", Second_List)
    Second_List.sort()
    print ("sort second list:", Second_List)

print (list_method())

