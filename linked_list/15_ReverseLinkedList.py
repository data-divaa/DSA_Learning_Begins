'''
Author - Data - Divaa
Date - 17 -03- 2025
Desc - a python program to reverse the linked list
'''

class Node:
    def __init__(self,k):
        self.key = k
        self.next = None

def ReverseList(head):
    curr = head
    prev = None

    while curr != None:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next

    return prev


def printList(head):
    curr = head
    while curr != None:
        print(curr.key)
        curr = curr.next
    print()


head = Node(10)
head.next = Node(20)
head.next.next = Node(30)
head.next.next.next = Node(40)

printList(head)

head = ReverseList(head)
print("after:")
printList(head)
