'''
Date - 13 - May - 2025
Author - Data-Divaa
Desc - given a sorted array.count the occurence of the 1
'''


#helper function defintion
def find_first(lst):
    l = 0
    r = len(lst) - 1
    first = -1
    while l <= r:
        mid = l + (r - l) // 2
        if lst[mid] < 1:
            l = mid + 1
        elif lst[mid] > 1:
            r = mid - 1
        else:
            first = mid
            r = mid - 1
    return first
def find_last(lst):
    l = 0
    r = len(lst) - 1
    last = -1
    while l <= r:
        mid = l + (r - l) // 2
        if lst[mid] < 1:
            l = mid + 1
        elif lst[mid] > 1:
            r = mid -1
        else:
            last = mid
            l = mid + 1
    return last


#main function defintion
def count1(lst):
    first = find_first(lst)
    last = find_last(lst)

    if first != -1 and last != -1:
        return (last - first) + 1
    else:
        return -1


#fetching data
lst = list(map(int,input("enter your number list :").split()))


#final function call
if count1(lst) == -1:
    print("1's has not been found in the array ",lst)
else:
    print("total number of 1 in the array",lst,":",count1(lst))
