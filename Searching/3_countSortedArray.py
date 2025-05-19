'''
Date - 09 - May - 2025
Author - Data-Divaa
Desc - given a sorted array. count the occurence of the element provided
'''


def find_first(lst,target):
    l = 0
    r = len(lst) - 1
    first = -1
    while l <= r:
        mid = l + (r - l)//2
        if lst[mid] == target:
            first = mid
            r = mid - 1
        elif lst[mid] < target:
            l = mid + 1
        else:
            r = mid -1
    return first



def find_last(lst,target):
    l = 0
    r = len(lst) - 1
    last = -1
    while l <= r:
        mid = l + (r - l)//2
        if lst[mid] == target:
            last = mid
            l = mid + 1
        elif lst[mid] < target:
            l = mid + 1
        else:
            r = mid - 1
    return last

def Count(lst,target):
    first = find_first(lst,target)
    if first == -1:
        return 0
    else:
        return find_last(lst,target) -  first +1


lst = list(map(int,input("enter the list (space seperated):").split()))

target = int(input("enter the number to be found"))


print(Count(lst,target))
