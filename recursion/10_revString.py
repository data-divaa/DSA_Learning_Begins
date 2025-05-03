'''
Date - 03 - May - 2025
Author - Data-Divaa
Desc - Write a recursive function that returns the reversed version of a string.
'''

#function definition
def RevStr(string):
    #base case
    if len(string) == 0:
        return string
    #recursion call
    return RevStr(string[1:]) + string[0]

#fetching the inputs
string = input("enter your string :")

#function call
print(string,"reversed :",RevStr(string))
