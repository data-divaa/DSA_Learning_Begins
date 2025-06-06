'''
Date - 06 -june - 2025
Author - Data-Divaa
Desc - given two unsorted arrays sorted them into one array with the help of merge sort algorithm.
'''


def mergeTwoUnsortedArray(l1,l2):
    i,j = 0,0
    lst = []
    while i < len(l1) and j < len(l2):
        if l1[i] < l2[j]:
            lst.append(l1[i])
            i += 1
        else:
            lst.append(l2[j])
            j += 1

    while i < len(l1):
        lst.append(l1[i])
        i += 1

    while j < len(l2):
        lst.append(l2[j])
        j += 1


    return lst

l1 = list(map(int,input("enter the first unsorted array (space seperated):").split()))

l2 = list(map(int,input("enter the second unsorted array (space seperated):").split()))



print("merged sorted array :",mergeTwoUnsortedArray(l1,l2))
