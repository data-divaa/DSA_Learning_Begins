'''
Date - 08 -june - 2025
Author - Data-Divaa
Desc - given two sorted array . give the intersection of the two sorted array in increasing order
'''

def SortInter(l1,l2):
    i,j = 0,0
    out = []
    while i < len(l1) and j < len(l2):
        if i > 0 and l1[i] == l1[ i-1]:
            i += 1
            continue
        if j > 0 and l2[j] == l2 [j -1]:
            j += 1
            continue

        if l1[i] < l2[j]:
            i += 1
        elif l1[i] > l2[j]:
            j += 1
        else:
            out.append(l1[i])
            i += 1
            j +=1

    return out



l1 = list(map(int,input("enter the first sorted array (space sepearted):").split()))
l2 = list(map(int,input("enter the second sorted array (space sepearted):").split()))

print(SortInter(l1,l2))
