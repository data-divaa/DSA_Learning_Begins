'''
Date - 29 - April - 2025
Author - Data-Divaa
Desc - Use recursion to print numbers from 1 to N in ascending order
'''

#function defintion
def printAsc(n):
    #base case
    if n == 0:
        return 0
    #recursive call
    printAsc(n-1)

    print(n, end = " ")


#fetching input
n = int(input("enter the number :"))

#fuction call
print("the number from  1 to ",n,"in ascending order:")
printAsc(n)
