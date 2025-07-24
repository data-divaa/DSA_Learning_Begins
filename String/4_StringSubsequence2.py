'''
Date - 23 -july - 2025
Author - Data-Divaa
Desc - given two strngs s1, s2 check if the string s2 is a subsequence of s1 with the help of recursion
'''

#function defintion
def RecursionSubsequenceStr(s1,s2,i,j):
    if i == 0:
        return False
    if j == 0:
        return True
    if s1[i-1] == s2[j-1]:
        return RecursionSubsequenceStr(s1,s2,i-1,j-1)
    else:
        return RecursionSubsequenceStr(s1,s2,i-1,j)


#fetching inputs
s1 = input("enter the string to check subsequence from :")
s2 = input("enter the string to check  if it is subsequence:")

i = len(s1)
j = len(s2)

#function call
if RecursionSubsequenceStr(s1,s2,i,j):
    print(s2, "is sbsequence of ",s1)
else:
    print(s2,"is not a sunsequence of ", s1)
