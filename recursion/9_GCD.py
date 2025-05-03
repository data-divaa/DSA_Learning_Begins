'''
Date - 29 - April - 2025
Author - Data-Divaa
Desc - Write a recursive function to compute the GCD of two numbers.
'''

#function defintion
def GCD(a,b):
    #base case
    if b == 0:
        return a
    #recursive call
    return GCD(b, a%b)

#fetching inputs
a,b = map(int,input("enter both the number (space separted):").split())

#function call
print("GCD of ",a,"and ",b,":",GCD(a,b))
