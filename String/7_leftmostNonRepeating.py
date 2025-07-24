'''
Date - 23 -july - 2025
Author - Data-Divaa
Desc - return the leftmost Non -repeating character from the string
'''
#importing
import sys

#function definition
def LeftmostNonrepeating(s):
    temp = [-1] * 256
    for i in range(len(s)):
        if temp[ord(s[i])] == -1:
            temp[ord(s[i])] = i
        else:
            temp[ord(s[i])] = -2
    res = sys.maxsize
    for i  in range(256):
        if temp[i] >= 0:
            res = min(res,temp[i])
    if res == sys.maxsize:
        return -1
    else:
        return res


#fetching inputs
s = input("enter string to look for leftmost non - repeating character :")

#function call
if LeftmostNonrepeating(s) != -1:
    print("leftmost Non - repeating character is at index ",LeftmostNonrepeating(s))
else:
    print("there are no repeating charcters in the given string")
