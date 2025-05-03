'''
Date - 03 - May - 2025
Author - Data-Divaa
Desc - Write a recursive function that returns the reversed version of a string.
'''


def RevStr(string):
    if len(string) == 0:
        return string
    return RevStr(string[1:]) + string[0]

string = input("enter your string :")

print(string,"reversed :",RevStr(string))
