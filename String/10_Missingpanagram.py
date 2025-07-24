'''
Date - 24 -july - 2025
Author - Data-Divaa
Desc - given a string check if it is panagram or not if not what is missing if the input is given in lower case and in lexigraphic so should be the ouptut
'''

#function defintion
def MissingPanagram(s):
    seen = [0] * 26
    for i in s:
        if i.isalpha():
            j = i.lower()
            idx = ord(j) - ord('a')
            seen[idx] = 1


    missing = ""
    for k in range(26):
        if seen[k] == 0:
            missing += chr(k + ord('a'))

    if not missing:
        return -1
    else:
        return "".join(missing)

#fetching input
s = input("enter the string to check for panagram (in lower case and in lexigraphic): ")

#FUNCTION call
if MissingPanagram(s) == -1:
    print(s,"is  a panagram")
else:
    print(s,"is not a panagram", "the missing characters in the panagrama are :",MissingPanagram(s))
