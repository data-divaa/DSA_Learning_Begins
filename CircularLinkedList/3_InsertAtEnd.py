'''
Date - 31 -7 - 2025
Author - Data - Divaa
Desc - insert a key at the end of a circular linked list and return the head
'''

class Node:
    def __init__(self,key):
        self.key = key
        self.next = None

def InsertAtEnd(head,key):
    temp = Node(key)
    if head == None:
        temp.next = temp
        return temp
    else:
        temp.next = head.next
        head.next = temp
        head.key , temp.key= temp.key, head.key
        return temp

def printCirList(head):
    if head == None:
        return
    print(head.key, end = " ")
    curr = head.next
    while curr != head:
        print(curr.key, end = " ")
        curr = curr.next

    print()

head = Node(10)
head.next = Node(20)
head.next.next = Node(30)
head.next.next.next = head

printCirList(head)

head = InsertAtEnd(head,40)

printCirList(head)
