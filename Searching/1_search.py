'''
Date - 08 - May - 2025
Author - Data-Divaa
Desc - you are given a sorted array and a number if the number is found in the array return its index if not return -1.
'''

#function defintion
def Search(lst,n):
    l = 0
    r = len(lst) - 1
    while l <= r:
        mid = l + (r - l) //2
        if lst[mid] == n:
            return mid
        elif lst[mid] < n:
            l = mid + 1
        else:
            r = mid -1
    return -1


#fetching data
lst = list(map(int,input("enter the sorted list (space seperated) :").split()))

n = int(input("enter the number to found in the sorted array:"))


#function call
if Search(lst,n) == -1:
    print("number",n,"not found in",lst)
else:
    print("number",n,"found at index",Search(lst,n),"in the sorted array",lst)
