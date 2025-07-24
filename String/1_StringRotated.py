'''
Date - 23 -july - 2025
Author - Data-Divaa
Desc - check if the two given strings are rotation of each other
'''

#function defintion
def RotatedString(s1,s2):
    if len(s1) != len(s2):
        return False
    res = ""
    res = s1 + s1
    return res.find(s2) != -1

#fetching inputs
s1,s2 = input("enter the two given strings to check rotation (space seperated):").split()

#function call
if RotatedString(s1,s2) != True :
    print(s1 ," and ",s2, "are not rotated version if each other")
else:
    print(s1,"and",s2, "are rotated version of each other")
