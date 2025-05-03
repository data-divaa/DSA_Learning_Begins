'''
Date - 27 - April - 2025
Author - Data-Divaa
Desc - Given an integer n, return the sum of its digits using recursion.
'''

#function defintion
def SumOfDigit(n):
    #base case
    if n == 0:
        return 0
    #recursion call
    return n % 10+ SumOfDigit(n // 10)


#fetching inputs
n = int(input("enter your number :"))

#function call
print("sum of digit ",n, "is : ",SumOfDigit(n))
