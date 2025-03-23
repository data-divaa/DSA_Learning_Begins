'''
Author - Data - Divaa
Date - 21 -03- 2025
Desc - a python program to check palindrome numbers
'''


class Node:
    def __init__(self,k):
        self.data = k
        self.next = None

def isPalindrome(head):
        #code here
        fast = head
        slow = head

        #middle
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        #reverse second half
        prev = None
        while slow:
            temp = slow.next
            slow.next = prev
            prev = slow
            slow = temp


        #check for palindrome
        left , right = head , prev
        while right:
            if left.data != right.data:
                return False
            left = left.next
            right = right.next
        return True



head = Node(1)
head.next = Node(2)
head.next.next = Node(2)
head.next.next.next= Node(1)


print(isPalindrome(head))
