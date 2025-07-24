'''
Date - 23 -july - 2025
Author - Data-Divaa
Desc - given two strings check if they are anagram of each other or not
'''

#function definition
def StringAnagram(s1,s2):
    if len(s1) != len(s2):
        return False
    count = [0] * 256
    for i in range(len(s1)):
        count[ord(s1[i])] += 1
        count[ord(s2[i])] -= 1
    for j in count :
        if j != 0:
            return False
    return True


#fetching inputs
s1 , s2 = input("enter the strings (space sepearted) to check for anagram ").split()

#function call
if StringAnagram(s1,s2):
    print(s1, "and", s2 ,"are anagram")
else:
    print(s1, "and",s2,"are not anagram")
