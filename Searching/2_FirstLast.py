'''
Date - 09 - May - 2025
Author - Data-Divaa
Desc - given a sorted array and a number. print the first and last occurence of the number found in the array. if the number is not found at all print -1 for both .
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


lst = list(map(int,input("enter the list (space seperated):").split()))

target = int(input("enter the number to be found"))

first = find_first(lst,target)
last = find_last(lst,target)


if first == -1:
    print("element not found")
else:
    print("first occurence:",first)
    print("last occurence:",last)
