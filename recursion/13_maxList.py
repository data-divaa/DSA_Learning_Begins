'''
Date - 05 - May - 2025
Author - Data-Divaa
Desc -Write a recursive function to find the maximum value in a list.
Example: find_max([3, 5, 2, 9, 1]) → 9
'''

#function definition
def FindMax(lst):
    if len(lst) <= 1:
        return lst[0]
    max_rest = FindMax(lst[1:])
    return lst[0] if lst[0] > max_rest else max_rest


#fetching inputs
lst = list(map(int,input("enter the number list (space separted):").split()))

#function call
print("the maximum out of the list",lst,":",FindMax(lst))
