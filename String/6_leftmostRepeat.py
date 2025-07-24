'''
Date - 23 -july - 2025
Author - Data-Divaa
Desc - return the leftmost repeating character from the string
'''

#function defintion
def LeftmostRepeat(s):
    temp = [False] * 256
    res = -1
    for i in range(len(s)-1,-1,-1):
        if temp[ord(s[i])] == True:
            res = i
        else:
            temp[ord(s[i])] = True
    return res

#fetching input
s = input("enter the string to look for the leftmost repeating strng:")

#function call
if LeftmostRepeat(s) != -1:
    print("leftmost repeating character is at index ",LeftmostRepeat(s))
else:
    print("there are no repeating charcters in the given string")
