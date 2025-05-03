'''
Date - 26 - April - 2025
Author - Data-Divaa
Desc - write a recursive function to calculate the factorial of a given number n.
'''

#function definition
def factorial(n):
    #base case
    if n == 0 or n == 1:
        return 1
    #recursive call
    return n * factorial(n-1)

#fetching input
n = int(input("enter the number :"))

#function call
print("the factorial of number ",n," :" , factorial(n))
