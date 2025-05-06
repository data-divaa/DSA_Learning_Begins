'''
Date - 05 - May - 2025
Author - Data-Divaa
Desc - Write a recursive function that returns the sum of all elements in a list.
'''

#function defintion
def SumOfArray(lst):
    if not lst:
        return 0
    return lst[0] + SumOfArray(lst[1:])

#fetching inputs
lst = list(map(int,input("enter the number list (space separted) :").split()))


#function call
print("the sum of element of list",lst,":",SumOfArray(lst))
