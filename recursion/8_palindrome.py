'''
Date - 29 - April - 2025
Author - Data-Divaa
Desc - Use recursion to check for palindrome
'''

#function definition
def palindrome(string):
    #base case
    if len(string) <= 1:
        return True
    #false case
    if string[0] != string[-1]:
        return False
    #recursive function
    return palindrome(string[1:-1])

#fetching inputs
string = input("enter the string :")

#function call
if palindrome(string) == True:
    print("Yes, it's a palindrome")
else:
    print("No, it's not a palindrome")
