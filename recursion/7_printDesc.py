'''
Date - 29 - April - 2025
Author - Data-Divaa
Desc - Use recursion to print numbers from N to 1 in descending order
'''

#function defintion
def printAsc(n):
    #base case
    if n == 0:
        return 0
    print(n, end = " ")
    #recursive call
    printAsc(n-1)


#fetching input
n = int(input("enter the number :"))

#fuction call
print("the number from  1 to ",n,"in descending order:")
printAsc(n)
