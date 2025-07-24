'''
Date - 24 -july - 2025
Author - Data-Divaa
Desc - given a string check if it is panagram or not
'''

#function defintion
def StringPanagram(s):
    seen = [0] * 26
    for i in s:
        if i.isalpha():
            j = i.lower()
            idx = ord(j) - ord('a')
            if seen[idx] == 0:
                seen[idx] += 1
    for j in seen:
        if j == 0:
            return False
    return True

#fetching inputs
s = input("enter the string to check for panagram:")

#function call
if StringPanagram(s):
    print(s,"is a panagram")
else:
    print(s,"is not a panagram")
