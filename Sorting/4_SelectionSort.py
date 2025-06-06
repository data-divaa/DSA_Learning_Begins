'''
Date - 26 - may - 2025
Author - Data-Divaa
Desc - given a unsorted array sort it into an increasing order with the help of selection sort algorithm
'''


#function defintion
def SelectionSort(lst):
    n = len(lst)

    for i in range(n-1):
        min_in = i
        for j in range(i+1,n):
            if lst[j] < lst[min_in]:
                min_in = j
        lst[min_in] , lst[i] = lst[i],lst[min_in]
    return lst


#fetching input
lst = list(input("enter the unsorted array(space seperated) :").split())

#function call
print(SelectionSort(lst))
