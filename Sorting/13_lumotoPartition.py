'''
Date - 15 -june - 2025
Author - Data-Divaa
Desc - given an unsorted array use lumoto partition for sorting
'''

#function defintion
def LumotoPartition(lst,low,high):
    pivot = lst[high]
    i = low -1
    for j in range(low,high):
        if lst[j] <= pivot:
            i += 1
            lst[j],lst[i] = lst[i],lst[j]
    lst[i+1],lst[high] = lst[high] , lst[i+1]
    return i +1


def QuickSort(lst,low,high):
    if low < high:
        pi = LumotoPartition(lst,low,high)

        QuickSort(lst,low,pi-1)
        QuickSort(lst,pi+1,high)


#fetching input
lst = list(map(int,input("enter the elements of the list (space sepearted):").split()))


#function call
QuickSort(lst,0,len(lst)-1)
print(lst)
