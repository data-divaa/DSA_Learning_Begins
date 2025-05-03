'''
Date - 27 - April - 2025
Author - Data-Divaa
Desc - Implement a recursive function that calculates a raised to the power b.
'''

#function definition
def power(n,m):
    #base case
    if m == 0:
        return 1
    #recusrion call
    return n * power(n , m-1)

#fetching data
n,m = map(int,input("enter the number and the power to be raised (space separted):").split())

#function call
print("when ",n,"is raised to power", m, "it becames",power(n,m))
