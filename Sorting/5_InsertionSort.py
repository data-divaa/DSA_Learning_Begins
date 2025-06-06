'''
Date - 28 - may - 2025
Author - Data-Divaa
Desc - given a unsorted array sort it into an increasing order with the help of insertion sort algorithm
'''

#function defintion
def InsertionSort(lst):
    for i in range(1,len(lst)):
        x = lst[i]
        j = i-1

        while j >= 0 and x < lst[j]:
            lst[j+1] = lst[j]
            j = j -1

        lst[j+1] = x
    return lst


#fetching inputs
lst = list(map(int,input("enter your unsorted array (space seperated):").split()))


#function call
print("after the insertion sort :",InsertionSort(lst))
