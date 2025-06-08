'''
Date - 08 -june - 2025
Author - Data-Divaa
Desc - given two sorted array . give the union of the tw sorted array in increasing order
'''


def SortUnion(l1,l2,n,m):
    i, j = 0,0
    out = []
    while i < n and  j <m:
        if l1[i] < l2[j]:
            if not out or out[-1] != l1[i]:
                out.append(l1[i])
            i += 1
        elif l2[j] < l1[i]:
            if not out or out[-1] != l2[j]:
                out.append(l2[j])
            j += 1
        else:
            if not out or out[-1] != l1[i]:
                out.append(l1[i])
            i += 1
            j += 1

    while i < n :
        if out[-1] != l1[i]:
            out.append(l1[i])
        i += 1

    while j < m:
        if out[-1] != l2[j]:
            out.append(l2[j])
        j +=1
    return out            


n,*l1 = list(map(int,input("enter length of the array  and the first sorted array (space sepearated):").split()))
m , *l2 = list(map(int,input("enter length of the  array the second sorted array (space seperated):").split()))


print(SortUnion(l1,l2,n,m))
