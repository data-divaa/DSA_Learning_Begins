'''
Date - 31 -7 - 2025
Author - Data - Divaa
Desc - delete the node at kth position and return the new circular linkd list
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

def Del_k(head,k):
    if head == None:
        return
    elif k == 1:
        return Del_k(head)
    else:
        curr = head
        for i in  range(k-2):
            curr = curr.next
        curr.next = curr.next.next
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
head.next.next.next = Node(40)
head.next.next.next.next = Node(50)
head.next.next.next.next.next = head


printCirList(head)

head = Del_k(head,3)

printCirList(head)
