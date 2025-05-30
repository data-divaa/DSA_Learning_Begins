'''
Author - Data - Divaa
Date - 17 -03- 2025
Desc - a python program to reverse the linked list using recurvion
'''

class Node:
    def __init__(self, k):
        self.key = k
        self.next = None


def reverseList(curr,prev = None):
    if curr == None:
        return prev

    next = curr.next
    curr.next = prev

    return reverseList(next,curr)



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

head = reverseList(head)

printList(head)
