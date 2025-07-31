'''
Date - 31 -7 - 2025
Author - Data - Divaa
Desc - create a circular linked list and print it
'''

class Node:
    def __init__ (self,k):
        self.key = k
        self.next = None

def printClrList(head):
    #check for empty list
    if head == None:
        return None
    print(head.key , end= " ")
    curr = head.next
    while curr != head:
        print(curr.key,end= " ")
        curr = curr.next

head = Node(10)
head.next = Node(40)
head.next.next = Node(89)
head.next.next.next = head

#function call
printClrList(head)
