'''
Date - 23 -july - 2025
Author - Data-Divaa
Desc - reverse the words of the string
'''

#helper function defintion
def reverseWord(s,b,e):
    while b < e:
        s[b],s[e] = s[e],s[b]
        b += 1
        e -= 1

#main function defintion
def reverseString(s):
    n = len(s)
    b = 0
    for e in range(n):
        if s[e] == " ":
            reverseWord(s,b,e-1)
            b = e + 1
    reverseWord(s,b,n-1)
    reverseWord(s,0,n-1)

#fetching inputs
s = list(input("enter the string to reverse words from (space seperated):"))


#function call
print("before reversing : ","".join(s))
reverseString(s)
print("after reversing : ","".join(s))
