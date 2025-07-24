'''
Date - 23 -july - 2025
Author - Data-Divaa
Desc - check for palindrome strings
'''

#function definition
def palindromeString(s):
    if len(s) == 1:
        return True
    l,r = 0 , len(s)-1
    while l <= r:
        if s[l] != s[r]:
            return False
        else:
            l += 1
            r -= 1
    return True

#fetching inputs
s = input("enter the string to check palindrome :")

#function call
if palindromeString(s):
    print(s,"is a palindrome")
else:
    print(s,"is not a palindrome")
