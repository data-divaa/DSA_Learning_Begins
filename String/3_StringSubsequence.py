'''
Date - 23 -july - 2025
Author - Data-Divaa
Desc - given two string s1, s2 check if s2 is a subsequence of s1
'''

#function definition
def StringSubsequence(s1,s2):
    i,j = 0,0
    while (i < len(s1) and j < len(s2)):
        if s1[i] == s2[j]:
            i += 1
            j += 1
        else:
            i += 1
    if j == len(s2) :
        return True
    else:
        return False

#fetching inputs
s1 = input("enter the string to check subsequence from :")
s2 = input("enter the string to check  if it is subsequence:")


#function call
if StringSubsequence(s1,s2):
    print(s2, "is a subsequence of ", s1)
else:
    print(s2,"is not a subsequence of ",s1)
