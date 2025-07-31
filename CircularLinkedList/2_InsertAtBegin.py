'''
Date - 31 -7 - 2025
Author - Data - Divaa
Desc - insert a key at the beginning of a circular linked list and return the new head
'''

class Node:
    def __init__(self,key):
        self.key = key
        self.next = None

def InsertAtBegin(head,key):
    temp = Node(key)
    if head == None:
        temp.next = temp
        return temp
    else:
        temp.next = head.next
        head.next = temp
        temp.key, head.key = head.key , temp.key
        return head

def printCirList(head):
    if head == None:
        return

    print(head.key , end = " ")
    curr = head.next
    while curr != head:
        print(curr.key, end = " ")
        curr = curr.next

    print()

head = Node(10)
head.next = Node(12)
head.next.next = Node(16)
head.next.next.next = head



printCirList(head)

head = InsertAtBegin(head ,5)

printCirList(head)
