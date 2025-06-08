'''
Date - 07 -june - 2025
Author - Data-Divaa
Desc - given a unsorted array sort it with the help of merge sort algorithm
'''


#helper function defintion
def MergeSubArrays(lst,low,high,mid):
    l1 = lst[low:mid+1]
    l2 = lst[mid+1 : high +1]

    i,j = 0,0
    k = low
    while i < len(l1) and j < len(l2):
        if l1[i] < l2[j]:
            lst[k] = l1[i]
            i += 1
            k += 1
        else:
            lst[k] = l2[j]
            j += 1
            k += 1

    while i < len(l1):
        lst[k] = l1[i]
        i += 1
        k += 1

    while j < len(l2):
        lst[k] = l2[j]
        j += 1
        k += 1




#main function defintion
def MergeSort(lst,l,r):
    if l < r:
        m = l +(r-l)//2
        MergeSort(lst,l,m)
        MergeSort(lst,m+1,r)
        MergeSubArrays(lst,l,r,m)



#fetching inputs
lst = list(map(int,input("enter the unsorted array (s]pace seperated):").split()))

low,high = map(int,input("enter the low and high (space sepearted):").split())


#function call
MergeSort(lst,low,high)
print("sorted array:",lst)
