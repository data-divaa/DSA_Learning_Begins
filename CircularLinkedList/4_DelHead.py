'''
Date - 31 -7 - 2025
Author - Data - Divaa
Desc - delete the head of the circular linked list and return the new head
'''

class Node:
    def __init__(self,key):
        self.key = key
        self.next = None

def DelHead(head):
    if head == None:
        return
    elif head.next == head:
        return None
    else:
        head.key = head.next.key
        head.next = head.next.next
        return head


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

head = DelHead(head)

printCirList(head)
