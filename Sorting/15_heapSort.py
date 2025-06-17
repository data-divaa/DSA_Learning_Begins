'''
Date - 16 -june - 2025
Author - Data-Divaa
Desc - given a unsorted array sort it with the help of heap Sort
'''


#function defintion
def Heapify(lst,n,i):
    largest = i
    left = 2 * i +1
    right = 2 * i + 2

    if left < n and lst[i] < lst[left]:
        largest = left
    if right < n and lst[largest] < lst[right]:
        largest = right
    if largest != i :
        lst[i], lst[largest] = lst[largest], lst[i]

        Heapify(lst,n,largest)


def HeapSort(lst):
    n = len(lst)

    for i in range((n//2)-1,-1,-1):
        Heapify(lst,n,i)


    for i in range(n-1,0,-1):
        lst[i],lst[0] = lst[0],lst[i]
        Heapify(lst,i,0)


#fetching input
lst = list(map(int,input("enter the list element space sepearted:").split()))


#function call
HeapSort(lst)
print("sorted list:",lst)
