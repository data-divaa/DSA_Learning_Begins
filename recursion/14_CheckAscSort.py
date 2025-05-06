'''
Date - 06 - May - 2025
Author - Data-Divaa
Desc - Determine recursively if a list is sorted in ascending order.
Example: is_sorted([1, 2, 3, 4]) → True
'''

#function definition
def CheckAsc(lst):
    #base case
    if len(lst) == 1:
        return True

    #recursion call
    if lst[0] < lst[1]:
         return CheckAsc(lst[1:])
    else:
        return False

#fetching inputs
lst = list(map(int,input("enter number list:(space seperated) ").split()))


#function call
if CheckAsc:
    print("the list provided is in ascending order")
else:
    print("the list provided is not arranged in descnding order")
