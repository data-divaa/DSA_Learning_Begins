'''
Date - 16 -june - 2025
Author - Data-Divaa
Desc - given a unsorted array sort it with the help of hoare's partition
'''

#functin defintion
def HoarePartition(lst,low,high):
    pivot = lst[low]
    i = low -1
    j = high +1
    while True:
        i += 1
        while lst[i] < pivot :
            i += 1

        j -= 1
        while lst[j] > pivot :
            j -= 1

        while i >= j :
            return j

        lst[i] , lst[j] = lst[j], lst[i]


def QuickSort(lst,low,high):
    if low < high :
        pi = HoarePartition(lst,low,high)
        QuickSort(lst,low,pi)
        QuickSort(lst,pi+1,high)


#fetching data
lst = list(map(int,input("enter the list (space sepearted):").split()))

#function call
QuickSort(lst,0,len(lst)-1)
print("sorted list :",lst)
